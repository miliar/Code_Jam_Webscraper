#!/usr/bin/python3

import sys

def parseLine(inputfile):
	return tuple([int(x) for x in inputfile.readline().split()])

def add(board, queue,n,m):
	seed = queue[0]
	del queue[0]
	direction = seed[2]
	added = 0
	toadd = None
	firstdir = direction
	if (direction == 0 and seed[0] + 1 < m):
		if (board[seed[0] + 1][seed[1]] == 0):
			added = 1
			board[seed[0] + 1][seed[1]] = 1
			toadd = (seed[0]+1, seed[1],0)
		
		direction += 1
	elif (direction == 0):
		direction = 1
	if (added == 0 and direction == 1 and seed[1] + 1 < n):
		if (board[seed[0]][seed[1] + 1] == 0):
			added = 1
			board[seed[0]][seed[1]+1] = 1
			toadd = (seed[0], seed[1]+1,0)

		direction += 1
	if (added == 0 and direction == 2 and seed[0] - 1 > -1):
		if (board[seed[0] - 1][seed[1]] == 0):
			added = 1
			board[seed[0] - 1][seed[1]] = 1
			toadd = (seed[0]-1, seed[1],0)
		direction += 1
	if (added == 0 and direction == 3 and seed[1] - 1 > -1):
		if (board[seed[0]][seed[1] - 1] == 0):
			added = 1
			board[seed[0]][seed[1] - 1] = 1
			toadd = (seed[0], seed[1] - 1,0)
		direction += 1
	#print(direction)	
	if (firstdir == direction):
		direction += 1
	if direction < 4:
		queue.insert(0,(seed[0],seed[1],direction))
	if (added == 1 and toadd != None):
		queue.append(toadd)
		 
	#print(queue)
	#for line in board:
	#	print(line)

	#print()
	return added,queue,board

def border(board, x, y, m, n):
	if (board[x][y] == 0):
		return 0
	if (x - 1 < 0 or board[x - 1][y] == 0):
		return 1
	if (x + 1 >= m or board[x + 1][y] == 0):
		return 1
	if (y - 1 < 0 or board[x][y-1] == 0):
		return 1
	if (y + 1 >= n or board[x][y + 1] == 0):
		return 1
	return 0

def orderqueue(queue,m,n):
	queue = queue
	newqueue = []
	while (len(queue) > 0):
		mindistance = float("inf")
		minindex = None
		middlex, middley = (m-1) / 2, (n-1) / 2 
		for y in queue:
			dist = (abs(y[0] - middlex) + abs(y[1] - middley))
			#print(dist)
			if dist < mindistance:
				mindistance = dist
				minindex = queue.index(y)
		#print(mindistance)
		newqueue.append(queue[minindex])
		del queue[minindex]
	
	return newqueue

def compute(n,m,k):
	board = [[0 for i in range(n)] for j in range(m)]
	queue = [(int(m/2), int(n/2),0)]
	board[queue[0][0]][queue[0][1]] = 1
	added = 1
	while (added < k):
		#print(queue)
		cadded,queue,board = add(board, queue,n,m)
		added += cadded
		#print(queue)
		queue = orderqueue(queue,m,n)
		#print(queue)
		#print("Done: {}/{}".format(added,k))
	#print("Board: {} x {}, {} stones".format(m,n,k))
	#for x in board:
		#print(x)

	borderlands = 0
	for i in range(m):
		for j in range(n):
			borderlands += border(board, i, j, m, n)

	return borderlands

if (len(sys.argv) == 2):
	text = open(sys.argv[1],'r')

	testCount = int(text.readline())
	
	for i in range(testCount):
		c,f,x = parseLine(text)
		if (x == 0):
			print("Case #{}: {}".format(i+1, 0))
		else:
			print("Case #{}: {}".format(i+1, compute(c,f,x)))
