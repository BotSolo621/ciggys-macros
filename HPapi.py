import requests

key = "" #Replace with you own DEV api key
PlayerName = "" #Replace with you own player name

def get_uuid(PlayerName):
    url = f"https://api.mojang.com/users/profiles/minecraft/{PlayerName}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["id"]
    else:
        print("Incorrect player name or Mojang's servers are down. Try again later.")
        exit(1)

def get_player_status(key, uuid):
    url = f"https://api.hypixel.net/status?key={key}&uuid={uuid}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["success"]:
            return data
        else:
            raise ValueError("API request failed. Check API key.")
        exit(2)
    else:
        raise ValueError("Failed to fetch status.")
    exit(3)

def check_lobby():
    uuid = get_uuid(PlayerName)
    data = get_player_status(key, uuid)
    session = data.get("session", {})
    success = data.get("success")
    online = session.get("online")
    game_type = session.get("gameType")
    mode = session.get("mode")
    return success, online, game_type, mode