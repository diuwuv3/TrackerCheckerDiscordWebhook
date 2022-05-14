import requests
import discord
import time


webhook = discord.Webhook.from_url(
    "YOUR WEBHOOK URL HERE",
    adapter=discord.RequestsWebhookAdapter())

tracker = {
    "Pirata Digital": {
        "url": "https://pirata.digital/register/null",
        "msg": "Os registros estão fechados! Você deve ser convidado para se registrar! Você foi redirecionado para a página de Login!"
    },
    
    "Generation Free": {
        "url": "https://generation-free.org/register/null",
        "msg": "Open Registration is Closed! You Must Be Invited To Register! You Have Been Redirected To Login Page!"
    }
}


while True:

    webhook.send(content="----------------------------------------------------")
    print("----------------------------------------------------")
    
    for i in range(len(tracker)):

        name = list(tracker)[i]
        url = tracker[list(tracker)[i]]["url"]
        req = requests.get(url)
        txt = req.text
        msg = tracker[list(tracker)[i]]["msg"]

        if req.status_code == 200:
            
            if msg in txt:
                print(f"INFO: {name} is closed.")
                webhook.send(content=f"{name} is closed...")
            else:
                print(f"INFO: {name} is open!")
                webhook.send(content=f"@everyone {name} is open! --> {url}")
        
        else:
            print(f"ERROR: {name} --> {req.status_code}")
            webhook.send(content=f"{name} --> Error {req.status_code}")
            
            
            time.sleep(1)

    
    webhook.send(content=f"`Time: {time.asctime()}`")
    print(f"Time: {time.asctime()}")

    webhook.send(content="----------------------------------------------------")
    print("----------------------------------------------------")

    time.sleep(3600)