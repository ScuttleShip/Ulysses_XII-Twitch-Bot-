#!/usr/bin/evn python
import config
import utility
import socket
import time
import re
import subprocess

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

try:
	s = socket.socket()
	s.connect((config.HOST, config.PORT))
	s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
	s.send("NICK {}\r\n".format(config.NICK).encode("utf-8"))
	s.send("JOIN {}\r\n".format(config.CHAN).encode("utf-8"))
	connected = True #Socket successfully connected
except Exception as e:
	print(str(e))
	connected = False #Socket failed to connect

def bot_loop():
	while connected:
		response = s.recv(1024).decode("utf-8")
		if response == "PING :tmi.twitch.tv\r\n":
			s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
			print("Pong")
		else:
			username = re.search(r"\w+", response).group(0)
			message = CHAT_MSG.sub("", response)
			print(username + ": " + response)
			for pattern in config.COMMANDS:
				if re.match(pattern[0], message):
					utility.chat(s,pattern[1])

			for pattern in config.COLOUR:
				if re.match(pattern[0], message):
					subprocess.call('sudo node tplight hex 192.168.0.21 #6441a5')

			for pattern in config.BAN_PAT:
				if re.match(pattern, message):
					utility.ban(s, username)
					break
		print(config.RATE)
		time.sleep(1 / config.RATE)

if __name__ ==  "__main__":
	bot_loop()
