#!/usr/bin/python

f = open('A-large.in')
inputline = f.readline()
numcase = int(inputline)

fout = open('bot_trust_large_result.txt', 'w')
movelist = []
colorlist = []
orangelist = []
bluelist = []
orangeindex = 0
blueindex = 0

m = 0
totalmove = 0
orangepos = 1
bluepos = 1


def checkmovebot(color, index):
	global orangepos, bluepos, orangeindex, blueindex
	if color == "O": 
		botpos = orangepos
		colorindex = orangeindex
		#print "   Orange togo to ",movelist[index]," from ", botpos
	else:
		botpos = bluepos
		colorindex = blueindex
		#print "   Blue togo to ",movelist[index]," from ", botpos
	if (botpos == movelist[index]):
		# presses button
		if color == "O":
			orangeindex = orangeindex + 1
		else:
			blueindex = blueindex + 1
		return True
	else:
		if botpos > movelist[index]:
			if color == "O":
				orangepos = orangepos - 1
			else:
				bluepos = bluepos - 1
		elif botpos < movelist[index]:
			if color == "O":
				orangepos = orangepos + 1
			else:
				bluepos = bluepos + 1
		return False

def movebot(color):
	global orangepos, orangeindex, bluepos, blueindex
	if color == "O":
		botpos = orangepos
		colorindex = orangeindex
		bot_totalmove = len(orangelist)
		nextmovelist = orangelist
	else:
		botpos = bluepos
		colorindex = blueindex
		bot_totalmove = len(bluelist)
		nextmovelist = bluelist
	#move bot if not in place
	#if color == "B":
	#	print "   --movebot------colorindex=",colorindex, " Color=",color," tot=",bot_totalmove
	if (colorindex < bot_totalmove):
		#print "   ------------colorindex=",colorindex, " Color=",color
		if botpos < nextmovelist[colorindex]:
			if color == "O":
				orangepos = orangepos + 1
			else:
				bluepos = bluepos + 1
		elif botpos > nextmovelist[colorindex]:
			if color == "O":
				orangepos = orangepos - 1
			else:
				bluepos = bluepos - 1

for i in range (0,numcase):
	line = f.readline()
	linelist = line.split()
	num_move = int(linelist[0])
	bluelist = []
	orangelist = []
	colorlist = []
	movelist = []
	for j in range (0,num_move):
		color = linelist[(j*2)+1]
		nextpos = int(linelist[(j*2)+2])
		#print "color =",color,"<- nextpos=",nextpos,"<-" 
		if color == "B":
			bluelist.append(nextpos)
		elif color == "O":
			orangelist.append(nextpos)
		colorlist.append(color)
		movelist.append(nextpos)
	#Start
	endgame = False
	totalpos = 0
	m = 0
	bluepos = 1
	orangepos = 1
	orangeindex = 0
	blueindex = 0
	totalmove = 0
	#print "Calculating case:",i," num_move=",num_move
	while (endgame == False):
		totalmove = totalmove + 1 
		#print "move=",totalmove," m=",m," orange=",orangepos,"blue=",bluepos
		cleared = checkmovebot(colorlist[m],m)
		if cleared:
			m = m + 1
			if m == num_move:
				endgame = True
			else:
				if (colorlist[m-1] == "B" ):
					movebot("O")
				else:
					movebot("B")
		else:
			if colorlist[m] == "B":
				movebot("O")
			else:
				movebot("B")
	answer = "Case #"+str(i+1)+": "+str(totalmove)	
	#print "Case #",i+1,": ",totalmove
	fout.write(answer)
	fout.write('\n')



f.close()
fout.close()
