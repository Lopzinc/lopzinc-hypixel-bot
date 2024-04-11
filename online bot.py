import requests
import discord
import asyncio
import json
intents = discord.Intents.all()
client = discord.Client(intents=intents)



try:
    with open('C:/Users/owene/Desktop/Desktop/Windows Setup/Files/Python/hypixel bot/messages/online_status.json', 'r') as file:
        message = json.load(file)
except FileNotFoundError:
    message = {}
async def save_message():
    with open('C:/Users/owene/Desktop/Desktop/Windows Setup/Files/Python/hypixel bot/messages/online_status.json', 'w') as file:
        json.dump(message, file)


async def update_statuses():
    while True:
        statuses = "The following information is only true if lop's computer is on, I will always have Discord open so you will know that way.\n\n"
        users = {
            "uchr2": "e3a1de69-38cf-4075-a404-ff3085794f98",
            "StrawCobra49152": "9a26dcfd-7776-49de-96e5-3a4c7cb0945a",
            "lopzinc": "b5f184bc-032a-4471-823d-94840d0d2e56",
            "qsleepzzz": "bacc12f7-2700-43d1-959a-b11f5a16f2b6",
            "Swixus": "a1c6b193-d7e2-4e0f-b368-717eb96fe28d",
            "Elinalise": "22a4e5b7-22c6-4794-9bf5-8c2753a3d0b6"
        }
        for username, uuid in users.items():
            response = requests.get(f"https://api.hypixel.net/v2/status?key={process.env.KEY}&uuid={uuid}").json().get("session", {})
            if response:
                gameType = response.get("gameType", "Unknown")
                if gameType.lower() == "unknown":
                    statuses += f"🔴 {username} is Offline 🔴\n"
                else:
                    mode = f", {response['mode'].replace('_', ' ').title()}" if 'mode' in response else ""
                    statuses += f"🟢 {username} is **Online** in {gameType.title()}{mode} 🟢\n"
            else:
                statuses += f"🔴 {username} is Offline 🔴\n"
        channel = client.get_channel(1127021720264527914)
        msg = await channel.send(statuses)
        await save_message()
        await asyncio.sleep(60)
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    client.loop.create_task(update_statuses())
client.run(process.env.TOKEN)
