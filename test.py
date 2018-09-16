import socket
import time
import sys
from command_parser import mainLoop
from skycrane.config import NICK, PASS, PORT, HOST  

interval = 5
words = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((HOST, PORT))
except :
    sys.exit("Did not connect to host\n")

# Connecting to chat via info
s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
s.send(bytes("JOIN #" + NICK + " \r\n", "UTF-8"))

print("Connected and starting")

# Parsing information twitch sends back to us
while True:
    line = str(s.recv(1024))
    if "End of /NAMES list" in line:
        break

# Collecting words in twitch chat in five second intervals
myTime = time.monotonic()
while True:   
    for line in str(s.recv(1024)).split('\\r\\n') :           
        parts = line.split(':')

        if len(parts) < 3:
            continue
        if parts[2] == "Please Leave ME" :
            s.send(bytes("PART #" + NICK + "\r\n", "UTF-8"))
            print("I AM LEAVING NOW")
        words.append(parts[2])
 
    if time.monotonic() > myTime + interval:
        # print(words)
        #call brenner function
        mainLoop(words)
        myTime = time.monotonic()
        words = []

