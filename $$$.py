import requests, threading, random, os, time
from colorama import init, Fore
from datetime import datetime
init()
threads = []
tokens = open('tokens.txt','r').read().splitlines()

def Spammer():
	for token in tokens:
		now = datetime.now()
		time = now.strftime("%H:%M:%S")
		rqs = requests.post(f'https://discordapp.com/api/v8/channels/{channel_id}/messages', json={"content": message,"tts": "false"}, headers={'authorization': token})
		response_data = rqs.json()
		if rqs.status_code == 200:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET}{Fore.GREEN}Sended Message With Succes")
		elif rqs.status_code == 401:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET} {Fore.RED}Token is invalid")
		elif rqs.status_code == 403:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET} {Fore.RED}" + response_data["message"])
		else:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET} {Fore.RED}Something is wrong")

def Joiner(invite):
	for token in tokens:
		now = datetime.now()
		time = now.strftime("%H:%M:%S")
		joiner_rqs = requests.post(f'https://discordapp.com/api/v8/invites/{invite}', headers={'authorization': token})
		if joiner_rqs.status_code == 200:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET}{Fore.GREEN}Succesfully Joined ")
		elif joiner_rqs.status_code == 404:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET} {Fore.RED}Unknow Invite ")
		else:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET} {Fore.RED}Something Wrong")
		

def Leaver(server_id):
	for token in tokens:
		now = datetime.now()
		time = now.strftime("%H:%M:%S")
		leaver_rqs = requests.delete(f'https://discord.com/api/v8/users/@me/guilds/{server_id}', headers={'authorization': token})
		print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET}{Fore.GREEN}Succesfully Leaved")


def Friender(name, discrim):
	for token in tokens:
		now = datetime.now()
		time = now.strftime("%H:%M:%S")
		Friender_rqs = requests.post('https://discordapp.com/api/v8/users/@me/relationships', headers = {'Authorization': token}, json = {'username':name,'discriminator':discrim})
		print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET}{Fore.GREEN}Friend Requests Sended To {name}#{discrim}")


def menu():
	mennu = """
\t\t\t      [1] Spammer [2] Joiner [3] Leaver  [4] Friender
	"""
	print(f"{Fore.LIGHTBLACK_EX}"+mennu)

def banner():
	os.system("cls")
	bannner = """
\t\t\t\t╔╦╗╦╔═╗╔═╗╔═╗╦═╗╔╦╗  ═╗ ╦  ╦═╗╔═╗╦╔╦╗╔═╗╦═╗
\t\t\t\t ║║║╚═╗║  ║ ║╠╦╝ ║║  ╔╩╦╝  ╠╦╝╠═╣║ ║║║╣ ╠╦╝
\t\t\t\t═╩╝╩╚═╝╚═╝╚═╝╩╚══╩╝  ╩ ╚═  ╩╚═╩ ╩╩═╩╝╚═╝╩╚═"""
	print(f"{Fore.LIGHTCYAN_EX}{bannner}")
banner()
menu()
choose = int(input(">"))
os.system("cls")
banner()
menu()
if choose == 1:
    channel_id = int(input("Channel id : "))
    message = str(input("Message : "))
    amount = int(input("How many thead : "))
    os.system("cls")
    banner()
    menu()
    print("")
    for i in range(amount):
        t = threading.Thread(target=Spammer)
        threads.append(t)
        t.start()
elif choose == 2:
    invite = str(input("Invite link : "))
    Joiner(invite)
elif choose == 3:
    server_id = str(input("Server id : "))
    Leaver(server_id)
    print("All tokens leaved server")
elif choose == 4:
	name = str(input("Username : "))
	discrim = str(input("Discriminator : "))
	Friender(name, discrim)
else:
    print("error")
