#! /usr/bin/python

import sys
import math

def print_grid(grid):
	print str_grid(grid)

def str_grid(grid):
	ret=""
	for i in xrange(len(grid)):
		ret+= "".join(grid[i])
		if i<(len(grid)-1):
			ret+="\n"
	return ret

def exec_test(R,C,M):
	Cc=C
	Rc=R
	Mc=M

	grid = []
	for i in xrange(R):
		grid.append(list("."*C))

	grid[0][0] = 'c'

	done=1
	while done==1:
		done=0
		while Mc>=Cc and Rc>3:
			for i in xrange(Cc):
				grid[Rc-1][i] = '*'
			Rc-=1
			Mc-=Cc
			done=1
		
		while Mc>=Rc and Cc>3:
			for i in xrange(Rc):
				grid[i][Cc-1] = '*'
			Cc-=1
			Mc-=Rc
			done=1

	if Mc>(Rc*Cc-1):
		return "Impossible"

	if Mc==0:
		return str_grid(grid)

	if Rc==3 and Cc==3:
		if Mc==1:
			grid[Rc-1][Cc-1] = '*'
			return str_grid(grid)
		elif Mc==2:
			return "Impossible"
		elif Mc>=3:
			for i in xrange(3):
				grid[Rc-1][i] = '*'
			Rc-=1
			Mc-=3
			if Mc==0:
				return str_grid(grid)

	if (Rc==2 and Cc>3) or (Cc==2 and Rc>3):
		assert Mc==1
		return "Impossible"

	if Mc==Rc*Cc-1:
		for i in xrange(Cc):
			for j in xrange(Rc):
				if grid[j][i]=='.':
					grid[j][i]='*'
		return str_grid(grid)

	if Rc==2 and Cc==2:
		return "Impossible"

	if Rc==2 and Cc==3:
		if Mc==1:
			return "Impossible"
		if Mc>2:
			return "Impossible"
		if Mc==2:
			grid[0][Cc-1] = '*'
			grid[1][Cc-1] = '*'
			return str_grid(grid)
	
	if Rc==3 and Cc==2:
		if Mc==1:
			return "Impossible"
		if Mc>2:
			return "Impossible"
		if Mc==2:
			grid[Rc-1][0] = '*'
			grid[Rc-1][1] = '*'
			return str_grid(grid)

	if Rc==1:
		for i in xrange(Mc):
			grid[0][Cc-1-i] = '*'
		return str_grid(grid)
	if Cc==1:
		for i in xrange(Mc):
			grid[Rc-1-i][0] = '*'
		return str_grid(grid)


	assert Mc<Cc
	assert Mc<Rc
	assert Rc>=3
	assert Cc>=3

	if Mc<=Rc-2:
		for i in xrange(Mc):
			grid[Rc-1-i][Cc-1] = '*'
		return str_grid(grid)

	if Mc<=Cc-2:
		for i in xrange(Mc):
			grid[Rc-1][Cc-1-i] = '*'
		return str_grid(grid)

	assert Rc==Cc
	assert Mc==Rc-1

	if Cc==3:
		return "Impossible"
	else:
		for i in xrange(Cc-2):
			grid[Rc-1][Cc-1-i] = '*'
		Rc-=1
		Mc-=Cc-2
		assert Mc==1
		grid[Rc-1][Cc-1] = '*'
		return str_grid(grid)

# ====== READ INPUT ====================================

assert len(sys.argv)>=2, "Need input file"
input_file = sys.argv[1]
fd = open(input_file, 'r')
fd_out = open(input_file+".out", 'w')
n = int(fd.readline().split()[0]) # Number of tests
for test in xrange(n):
	print "=== Test #%i ===" % (test+1)
	nums = fd.readline().split()
	(R,C,M) = map(lambda x: int(x), nums)
	ret = exec_test(R,C,M)
	strret = "Case #%i:\n%s" % ((test+1), str(ret))
	print strret
	fd_out.write(strret+"\n")

