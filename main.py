import requests, threading, random, os, time
from colorama import init, Fore
from datetime import datetime
init()
threads = []
tokens = open('tokens.txt','r').read().splitlines()

def Spammer():
	for token in tokens:
		time = datetime.now().strftime("%H:%M:%S")
		rqs = requests.post(f'https://discordapp.com/api/v8/channels/{channel_id}/messages', json={"content": message,"tts": "false"}, headers={'authorization': token})
		if rqs.status_code == 200:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET}{Fore.GREEN}Sended Message With Succes")
		elif rqs.status_code == 401:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET} {Fore.RED}Token is invalid")
		elif rqs.status_code == 403:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET} {Fore.RED}Eror")
		else:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET} {Fore.RED}Something is wrong")

def Joiner(invite):
	for token in tokens:
		time = datetime.now().strftime("%H:%M:%S")
		joiner_rqs = requests.post(f'https://discordapp.com/api/v8/invites/{invite}', headers={'authorization': token})
		if joiner_rqs.status_code == 200:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET}{Fore.GREEN}Succesfully Joined ")
		elif rqs.status_code == 401:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET} {Fore.RED}Token is invalid")
		elif joiner_rqs.status_code == 404:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET} {Fore.RED}Unknow Invite ")
		else:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET} {Fore.RED}Something Wrong")
		

def Leaver(server_id):
	for token in tokens:
		time = datetime.now().strftime("%H:%M:%S")
		leaver_rqs = requests.delete(f'https://discord.com/api/v8/users/@me/guilds/{server_id}', headers={'authorization': token})
		if leaver_rqs == 429 or 401:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET}{Fore.GREEN}Eror")
		else:
			print(f"{Fore.RED}[{Fore.RESET}{Fore.LIGHTBLACK_EX}{time}{Fore.RED}]{Fore.RESET}{Fore.GREEN}Succesfully Leaved")

def menu():
	mennu = """
\t\t\t            [1] Spammer [2] Joiner [3] Leaver  
	"""
	print(f"{Fore.LIGHTBLACK_EX}"+mennu)

def banner():
	os.system("cls")
	bannner = """
\t\t\t\t╔╦╗╦╔═╗╔═╗╔═╗╦═╗╔╦╗  ═╗ ╦  ╦═╗╔═╗╦╔╦╗╔═╗╦═╗
\t\t\t\t ║║║╚═╗║  ║ ║╠╦╝ ║║  ╔╩╦╝  ╠╦╝╠═╣║ ║║║╣ ╠╦╝
\t\t\t\t═╩╝╩╚═╝╚═╝╚═╝╩╚══╩╝  ╩ ╚═  ╩╚═╩ ╩╩═╩╝╚═╝╩╚═"""
	print(f"{Fore.LIGHTCYAN_EX}{bannner}")


while True:
	banner()
	menu()
	choose = int(input(">"))
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
	else:
	    print("error")
