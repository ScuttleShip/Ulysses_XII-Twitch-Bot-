HOST = "irc.chat.twitch.tv" # This is Twitchs IRC server
PORT = 6667 # Twitch IRC server listens on port 6667
NICK = "xxxxx" # Twitch username you're using for your bot
PASS = "xxxxx" # your Twitch OAuth token
CHAN = "#xxxx" # The channel you want your bot to join
RATE = (20/30.0) # Messages per second
BAN_PAT = [
	r"xxxx",
]
SUBSCRIBER = [
	[r"Thank you for being subscribed for"],
	[r"Thank you for gifting a sub to"],
	[r"Thank you for gifting a"],
]
CHEER = [
	[r"just cheered with"],
]
DONATION = [
	[r"Thank you for the donation of"],
]
FOLLOWER = [
	[r"Thank you for the follow!"],
]

COLOUR = [
	[r"!twitch","Changing the light to Twitch Purple"],
	[r"!green", "Changing the light to Green"],
]
COMMANDS = [
	[r"!invdiscord","Join the TI discord here: https://discord.gg/My9emf8"],
]
