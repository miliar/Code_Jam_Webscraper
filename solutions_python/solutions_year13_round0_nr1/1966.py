T=int(raw_input())
for i in xrange(T):
	hasDot=False
	r=0
	c=0
	boardX = [[0 for x in xrange(4)] for x in xrange(4)] 
	boardO = [[0 for x in xrange(4)] for x in xrange(4)] 
	for r in xrange(4):
		c=0
		for a in raw_input():
			if a == 'T':
				boardX[r][c] = 'X'
				boardO[r][c] = 'O'
			else:
				boardX[r][c] = a
				boardO[r][c] = a
				if a == '.':
					hasDot=True
			c=c+1
	raw_input()
	
	xw,ow=False,False
	#rows
	for r in xrange(4):
		count=0
		for c in xrange(4):
			if boardX[r][c]=='X':
				if count >= 0:
					count = count + 1
					if count == 4:
						xw=True	
				else:
					count = 0
			elif boardX[r][c]=='O':
				if count <= 0:
					count = count - 1
					if count == -4:
						ow=True
				else:
					count = 0
			else:
				count = 0
		count=0
		for c in xrange(4):
			if boardO[r][c]=='X':
				if count >= 0:
					count = count + 1
					if count == 4:
						xw=True
				else:
					count = 0
			elif boardO[r][c]=='O':
				if count <= 0:
					count = count - 1
					if count == -4:
						ow=True
				else:
					count = 0
			else:
				count = 0
	#columns
	for c in xrange(4):
		count=0
		for r in xrange(4):
			if boardX[r][c]=='X':
				if count >= 0:
					count = count + 1
					if count == 4:
						xw=True
				else:
					count = 0
			elif boardX[r][c]=='O':
				if count <= 0:
					count = count - 1
					if count == -4:
						ow=True
				else:
					count = 0
			else:
				count = 0
		count=0
		for r in xrange(4):
			if boardO[r][c]=='X':
				if count >= 0:
					count = count + 1
					if count == 4:
						xw=True
				else:
					count = 0
			elif boardO[r][c]=='O':
				if count <= 0:
					count = count - 1
					if count == -4:
						ow=True
				else:
					count = 0
			else:
				count = 0

	#diags
	count=0
	for r in xrange(4):
		c = r	
		if boardO[r][c]=='X':
			if count >= 0:
				count = count + 1
				if count == 4:
					xw=True
			else:
				count = 0
		elif boardO[r][c]=='O':
			if count <= 0:
				count = count - 1
				if count == -4:
					ow=True
			else:
				count = 0
		else:
			count = 0

	count=0
	for r in xrange(4):
		c = 3 - r	
		if boardO[r][c]=='X':
			if count >= 0:
				count = count + 1
				if count == 4:
					xw=True
			else:
				count = 0
		elif boardO[r][c]=='O':
			if count <= 0:
				count = count - 1
				if count == -4:
					ow=True
			else:
				count = 0
		else:
			count = 0

	count=0
	for r in xrange(4):
		c = r	
		if boardX[r][c]=='X':
			if count >= 0:
				count = count + 1
				if count == 4:
					xw=True
			else:
				count = 0
		elif boardX[r][c]=='O':
			if count <= 0:
				count = count - 1
				if count == -4:
					ow=True
			else:
				count = 0
		else:
			count = 0

	count=0
	for r in xrange(4):
		c = 3 - r	
		if boardX[r][c]=='X':
			if count >= 0:
				count = count + 1
				if count == 4:
					xw=True
			else:
				count = 0
		elif boardX[r][c]=='O':
			if count <= 0:
				count = count - 1
				if count == -4:
					ow=True
			else:
				count = 0
		else:
			count = 0
	
	if xw:
		print "Case #"+str(i+1)+": X won"
	elif ow:
		print "Case #"+str(i+1)+": O won"
	else:
		if not hasDot:
			print "Case #"+str(i+1)+": Draw"
		else:
			print "Case #"+str(i+1)+": Game has not completed"

