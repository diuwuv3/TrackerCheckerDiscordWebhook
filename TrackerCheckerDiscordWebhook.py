from config import *
import requests
import discord
import time


webhook = discord.Webhook.from_url(webhook_url, adapter=discord.RequestsWebhookAdapter())


while True:
    
    webhook_message = "---------------------------------------------------\n"
    print("---------------------------------------------------")
    
    for i in range(len(tracker)):

        name = list(tracker)[i]
        flag = tracker[name]["flag"]
        url = tracker[name]["url"]
        req = requests.get(url)
        txt = req.text
        msg = tracker[name]["msg"]

        if req.status_code == 200:
            if msg in txt:
                print(f"INFO: {name} is closed.")
                webhook_message = webhook_message + f":red_circle: - {name}{flag} is closed...\n"
                time.sleep(1)
            else:
                print(f"INFO: {name} is open!")
                webhook_message = webhook_message + f":green_circle: - {name}{flag} is open! --> {url}\n"
                time.sleep(1)
        else:
            print(f"ERROR: {name} --> {req.status_code}")
            webhook_message = webhook_message + f":orange_circle: - {name}{flag} --> Error {req.status_code}\n"
            time.sleep(1)

    webhook_message = webhook_message + f"`Time: {time.asctime()}`\n"
    webhook_message = webhook_message + "---------------------------------------------------"

    if "open" in webhook_message:
        webhook_message = webhook_message + "\n" + "||@everyone||"
    
    webhook.send(content=webhook_message)

    print(f"Time: {time.asctime()}")
    print("---------------------------------------------------")
    print()

    time.sleep(86400)