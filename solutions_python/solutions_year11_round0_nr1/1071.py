import re

inFile = open('A-large.in', 'r')
outFile = open('A-large-out.txt', 'w')

numTests = inFile.readline()
#print numTests,

idx = 1
for i in inFile.readlines():
	time = 0;
	orangeBot = 1 #position of orange
	blueBot = 1 #position of blue
	numButtons = i[0]
	pattern = i[2::]
	line = re.split('(\W+)', pattern)
	commands = []
	ojCommands = []
	blueCommands = []
	for j in range(len(line)):
		if line[j] == 'O':
			ojCommands.append((line[j], line[j+2]))
			commands.append((line[j], line[j+2]))
		elif line[j] == 'B':
			blueCommands.append((line[j], line[j+2]))
			commands.append((line[j], line[j+2]))
	while len(commands) > 0:
		#Move the blue bot
		#print "Blue Bot: " + str(blueBot)
		#print "Orange Bot: " + str(orangeBot)
		#print commands
		om = False
		bm = False
		op = False
		bp = False
		time += 1
		if len(blueCommands) > 0:
			if blueBot < int(blueCommands[0][1]):
				blueBot += 1
				bm = True
			elif blueBot > int(blueCommands[0][1]):
				blueBot -= 1
				bm = True
			else:
				# It is at the correct button
				bm = False
				if (blueCommands[0] == commands[0] and not bm and not op):
					bm = False
					blueCommands.pop(0)
					commands.pop(0)
					print "Blue pushes a button : " + str(time)
					bp = True
		# Move the orange Bot
		if len(ojCommands) > 0:
			if orangeBot < int(ojCommands[0][1]):
				orangeBot += 1
				om = True
			elif orangeBot > int(ojCommands[0][1]):
				orangeBot -= 1
				om = True
			else:
				#It is at the correct button
				om = False
				if (ojCommands[0] == commands[0] and not om and not bp):
					om = False
					ojCommands.pop(0)
					commands.pop(0)
					print "Orange pushes a button : " + str(time)
					op = True
					
	outString = "Case #" + str(idx) + ": " + str(time) + "\n"
	outFile.write(outString)
	idx += 1
	
inFile.close()
outFile.close()
