from Library import *
import math

def rwin(x, r, c):
	l = int(math.ceil(x / 2.0))
	if x >= 7: # chose an omino with a hole
		return True
	elif (r < x and c < x): # straight line FTW
		return True
	elif r == 0 or c == 0: # no box
		return True
	elif (r * c) % x != 0: # not enough space
		return True
	elif l > r or l > c: # L shape exceeds dimension
		return True
	else:
		return False

def solve(x, r, c):
	R = "RICHARD"
	G = "GABRIEL"
	if rwin(x, r, c):
		return R
	if x <= 3:
	    return G
	else:
		l = int(math.ceil(x / 2.0))
		if x + l == r + c:
			return R
		else:
			return G

lines = getLines("D-small-attempt0.in")
out = []

for i in range(int(lines[0])):
	
	values = [int(l) for l in lines[i + 1].split()]
	res = solve(values[0], values[1], values[2])
	out.append("Case #%d: %s"%(i + 1, res))

writeOutLines("out.txt", out)