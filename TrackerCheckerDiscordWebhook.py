import requests
import discord
import time


webhook = discord.Webhook.from_url(
    "", # YOUR WEBHOOK URL HERE
    adapter=discord.RequestsWebhookAdapter())

tracker = {
    "Generation Free": {
        "url": "https://generation-free.org/register/null",
        "msg": "Open Registration is Closed! You Must Be Invited To Register! You Have Been Redirected To Login Page!",
        "flag": ":flag_fr:"
    },
    "FL-Team": {
        "url": "https://flopload.cc/sbg_login_new.php",
        "msg": "Désolé, mais les inscriptions sont fermées.",
        "flag": ":flag_fr:"
    },
    "Pirata Digital": {
        "url": "https://pirata.digital/register/null",
        "msg": "Os registros estão fechados! Você deve ser convidado para se registrar! Você foi redirecionado para a página de Login!",
        "flag": ":flag_br:"
    },
    "Br Society": {
        "url": "https://brsociety.club/register/null",
        "msg": "Os registros estão fechados! Você deve ser convidado para se registrar! Você foi redirecionado para a página de Login!",
        "flag": ":flag_br:"
    },
    "Brasil Tracker": {
        "url": "https://brasiltracker.org/register.php",
        "msg": "Opa, somente registros com convite",
        "flag": ":flag_br:"
    },
    "Amigos Share Club": {
        "url": "https://cliente.amigos-share.club/account-signup.php",
        "msg": "Codigo do convite",
        "flag": ":flag_br:"
    },
    "Anime No Sekai": {
        "url": "https://www.ansktracker.net/signup.php",
        "msg": "No momento o tracker não aceita mais cadastros. Tente novamente outro dia.",
        "flag": ":flag_br:"
    },
    "AnimeBytes": {
        "url": "https://animebytes.tv/register/apply",
        "msg": "Invite Application",
        "flag": ":flag_gb:"
    },
    "GazelleGames": {
        "url": "https://gazellegames.net/register.php",
        "msg": "Registration is currently closed.",
        "flag": ":flag_gb:"
    }
}


while True:
    
    webhook.send(content="---------------------------------------------------")
    print("---------------------------------------------------")
    
    for i in range(len(tracker)):


        name = list(tracker)[i]
        flag = tracker[list(tracker)[i]]["flag"]
        url = tracker[list(tracker)[i]]["url"]
        req = requests.get(url)
        txt = req.text
        msg = tracker[list(tracker)[i]]["msg"]

        if req.status_code == 200:
            
            if msg in txt:
                print(f"INFO: {name} is closed.")
                webhook.send(content=f":red_circle: - {name}{flag} is closed...")
                time.sleep(1)
            else:
                print(f"INFO: {name} is open!")
                webhook.send(content=f"@everyone :green_circle: - {name}{flag} is open! --> {url}")
                time.sleep(1)

        else:
            print(f"ERROR: {name} --> {req.status_code}")
            webhook.send(content=f":orange_circle: - {name}{flag} --> Error {req.status_code}")
            time.sleep(1)

    webhook.send(content=f"`Time: {time.asctime()}`")
    print(f"Time: {time.asctime()}")

    webhook.send(content="---------------------------------------------------")
    print("---------------------------------------------------")

    time.sleep(3600)