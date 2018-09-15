directions = ['u','d','l','r']
commands = ["dip", "move"]

def parseyBoi(stringyBoi):
	splitBoi = stringyBoi.splitlines()
	for boi in splitBoi:
		words = boi.split(" ")
		for word in words:
			separate = word.split(":")
			if (separate[0] in commands):
				parseCommand(separate)

def parseCommand(command):
	if len(command) == 1 and command[0] == "dip":
		executeDip
	elif command[0] == "move" and len(command) == 2:
		(direction, distance) = parseDistance(command[1])
		if direction != "bad":
			executeMove(direction, distance)
	print "invalid command attempted: ", command[0]


def parseDistance(movement):
	if len(movement) < 2:
		return ("bad", 0)
	direction = "bad"
	firstLetter = movement[0]
	rest = movement[1:]
	if firstLetter in directions:
		direction = firstLetter
		try:
			float(rest)
			return direction, float(rest)
		except ValueError:
			return ("bad", 0)
	return ("bad, 0")

def executeDip():
	print "dip executed"
	return

def executeMove(direction, distance):
	print "move executed in direction: ", direction, "with distance: ", distance
	return

testText = """fkjdfhdfhdf j sf f u
boi what the fuck did you say to me
hfdhsdfjhsdfjh l
dip move
move:"""

parseyBoi(testText)
