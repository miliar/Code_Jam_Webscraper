#!/usr/bin/python

def rotateLeft(old):
	oldHeight = len(old)
	oldWidth = len(old[0])
	newHeight = oldWidth
	newWidth = oldHeight
	
	new = []
	for i in range(oldWidth):
		newLine = ""
		for l in old:
			newLine += l[i]
		new.append(newLine)
	new.reverse()
	return new

def rotateRight(old):
	oldHeight = len(old)
	oldWidth = len(old[0])
	newHeight = oldWidth
	newWidth = oldHeight
	
	new = []
	for i in range(oldWidth-1, -1, -1):
		newLine = ""
		for l in old:
			newLine += l[i]
		new.append(newLine)
	return new

def applyGravityToLine(l):
	pieces = ""
	for p in l:
		if p <> ".":
			pieces += p
	while len(pieces) < len(l):
		pieces += "."
	return pieces

def applyGravity(old):
	old = rotateRight(old) # last column is at the top now
	new = []
	for col in old:
		#print col
		newcol = applyGravityToLine(col)
		new.append(newcol)
	return rotateLeft(new)

def findWins(board, w):
	# try to find horizontal wins
	wins = []
	
	for row in board:
		consecutive = ""
		for i in range(len(row)):
			if len(consecutive) == 0 and row[i] <> ".":
				consecutive += row[i]
			elif len(consecutive) == 0:
				pass
			elif row[i] == consecutive[0]:
				consecutive += row[i]
			elif row[i] <> ".":
				consecutive = row[i]
			if len(consecutive) >= w:
				if consecutive[0] not in wins:
					wins.append(consecutive[0])
	
	rot = rotateRight(board)
	for col in rot:
		consecutive = ""
		for i in range(len(col)):
			if len(consecutive) == 0 and col[i] <> ".":
				consecutive += col[i]
			elif len(consecutive) == 0:
				pass
			elif col[i] == consecutive[0]:
				consecutive += col[i]
			elif col[i] <> ".":
				consecutive = col[i]
			if len(consecutive) >= w:
				if consecutive[0] not in wins:
					wins.append(consecutive[0])
	
	for y in range(len(board)):
		for x in range(len(board)):
			try:
				a = ""
				for z in range(w):
					a += board[y+z][x+z]
				b = ""
				for z in range(w):
					b += board[y+z][x-z]
				
				if a == a[0] * len(a):
					if a[0] not in wins:
						wins.append(a[0])
				if b == b[0] * len(b):
					if b[0] not in wins:
						wins.append(b[0])
			except:
				pass
	
	return wins

def prettyPrintWins(w):
	red = ("R" in w)
	blue = ("B" in w)
	if red and blue:
		return "Both"
	elif not red and not blue:
		return "Neither"
	elif red:
		return "Red"
	elif blue:
		return "Blue"

def stripNewline(l):
	return l.replace("\n", "")

f = open("A-large.in", "rU")

output = ""

cases = int(stripNewline(f.readline()))
for i in range(cases):
	line = stripNewline(f.readline())
	try:
		(numrows, k) = line.split(" ")
	except:
		continue
		
	numrows = int(numrows)
	k = int(k)
	board = []
	for j in range(numrows):
		board.append(stripNewline(f.readline()))
	board = rotateRight(board)
	board = applyGravity(board)
	wins = findWins(board, k)
	output += "Case #%i: %s\n" % (i+1, prettyPrintWins(wins))
	#output += str(k) + "\n"
	#for b in board:
	#	output += b + "\n"

f.close()
f = open("A-large.out", "w")
f.write(output)
f.close()