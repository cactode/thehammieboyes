import socket

TWITCH_USERNAME = "thehammieboyes"
TWITCH_OATH = "oauth:pvvnv26e9y88bro7yyjfbvp6orzdj3"

irc = socket.socket()
print("Connecting\n")
irc.connect(("irc.chat.twitch.tv", 6667))

print("Joining\n")
password = "PASS " + TWITCH_OATH + "\r\n"
irc.send(password.encode())
username = "NICK " + TWITCH_USERNAME + "\r\n"
irc.send(username.encode())
irc.send("JOIN ##thehammieboyes\r\n".encode())
irc.send("text: fuck you".encode())

