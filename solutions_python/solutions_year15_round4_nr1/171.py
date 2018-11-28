
import sys
import math
from collections import defaultdict

#f = open('A-large.in')
f = open('A-large.in')
cases = int(f.readline())

def checkUp(grid, rownum, colnum):
	newrownum = rownum - 1
	while newrownum >= 0 and grid[newrownum][colnum] == ".":
		newrownum -= 1
	if newrownum == -1:
		return False
	return True

def checkRight(grid, rownum, colnum):
	newcolnum = colnum + 1
	while newcolnum < len(grid[0]) and grid[rownum][newcolnum] == ".":
		newcolnum += 1
	if newcolnum == len(grid[0]):
		return False
	return True

def checkDown(grid, rownum, colnum):
	newrownum = rownum + 1
	while newrownum < len(grid) and grid[newrownum][colnum] == ".":
		newrownum += 1
	if newrownum == len(grid):
		return False
	return True

def checkLeft(grid, rownum, colnum):
	newcolnum = colnum - 1
	while newcolnum >= 0 and grid[rownum][newcolnum] == ".":
		newcolnum -= 1
	if newcolnum == -1:
		return False
	return True

def check(grid, rownum, colnum, ch):
	dirs = [checkUp(grid, rownum, colnum), checkRight(grid, rownum, colnum), checkDown(grid, rownum, colnum), checkLeft(grid, rownum, colnum)]
	if ch == "^":
		if dirs[0]:
			return (True, False)
		if True in dirs[1:]:
			return (False, True)
	elif ch == ">":
		if dirs[1]:
			return (True, False)
		if True in [dirs[0]] + dirs[2:]:
			return (False, True)
	elif ch == "v":
		if dirs[2]:
			return (True, False)
		if True in dirs[:2] + dirs[3:]:
			return (False, True)
	elif ch == "<":
		if dirs[3]:
			return (True, False)
		if True in dirs[:3]:
			return (False, True)
	return (False, False)
	

for i in xrange(1,cases+1):
	tochange = 0
	rows, cols = map(int, f.readline().rstrip().split())
	g = []
	for j in xrange(rows):
		r = f.readline().rstrip()
		g.append(list(r))
	
	ended = False
	for rnum, row in enumerate(g):
		for cnum, c in enumerate(row):
			if c != ".":
				t = check(g, rnum, cnum, c)
				#print rnum, cnum, t
				if t[0] == t[1] == False:
					ended = True
					print "Case #" + str(i) + ": IMPOSSIBLE"
					break
				if not t[0] and t[1]:
					tochange += 1
		if ended:
			break
	if not ended:
		print "Case #" + str(i) + ": " + str(tochange)

#rd = [[] for x in xrange(cols)]#defaultdict(lambda: [])
#cd = [[] for x in xrange(rows)]
#for rownum, row in enumerate(rows):
#	for colnum, c in enumerate(row):
#		if c != ".":
#			rd[]





#
#sys.stdin.readline().rstrip()

