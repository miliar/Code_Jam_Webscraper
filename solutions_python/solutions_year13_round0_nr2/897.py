# Python 2.7.2 (341e1e3821fff77db3bb5cdb7a4851626298c44e, Nov 23 2012, 19:06:15)
# [PyPy 1.9.0] on darwin
# (C) 2013 Dennis Bliefernicht

from copy import deepcopy
import numpypy as numpy

BASENAME="B"
TYPE="ex"
TYPE="sm0"
TYPE="la"
NODOUT=False

def checkrow(row):
	c = -2
	for x in row:
		if x == -1:
			continue
		elif c != -2 and x != c:
			return None
		else:
			c = x
	if c == -2:
		return None
	return c

def check_lawn(lawn):
	done = True
	# lawn all same size? / find min len
	c = lawn[0][0]
	mlen = 100
	for x in lawn:
		for y in x:
			mlen = min(y, mlen)
			if y != c:
				done = False
	if done:
		return True
	
	# find all row candidates for this length, grow them and repeat
	rows = []
	cols = []
	for x in range(len(lawn)):
		r = lawn[x]
		if mlen not in r:
			continue
		if checkrow(r):
			rows.append(x)
	for x in range(len(lawn[0])):
		c = lawn[:,x]
		if mlen not in c:
			continue
		if checkrow(c):
			cols.append(x)
			
	newlawn = numpy.array(lawn)
	for r in rows:
		for x in range(len(lawn[0])):
			if lawn[r][x] == mlen:
				newlawn[r][x] = mlen + 1
	for c in cols:
		for x in range(len(lawn)):
			if lawn[x][c] == mlen:
				newlawn[x][c] = mlen + 1
		
	if (newlawn == lawn).all():
		return False
		
	return check_lawn(newlawn)

def process():
	(w, h) = popintarray()
	lawn = []
	for x in range(w):
		lawn.append(popintarray())
		
	lawn = numpy.array(lawn)
		
	result = check_lawn(lawn)
	if result:
		return "YES"
	else:
		return "NO"

# ------------------------------------
# GCJ2013 framework stuff
# ------------------------------------
import time

lines = []
outf = None

def pop():
	global lines
	e = lines[0]
	lines = lines[1:]
	return e
	
def popint():
	return int(pop())
	
def popflt():
	return float(pop())
	
def popintarray():
	return map(lambda x: int(x), pop().split(" "))

def popstrarray():
	return pop().split(" ")
	
def outstr(s):
	global outf
	print s
	outf.write(s + "\n")

def dout(*vals):
	if NODOUT:
		return
	print "%",
	for v in vals:
		print str(v),
	print
	
def main():
	global lines
	case_count = int(pop())
	for case_number in range(case_count):
		result = process()
		outstr("Case #%d: %s" % (case_number+1, result))
	if len(lines) != 0:
		print "! %d lines remaining" % (len(lines))

if __name__ == "__main__":
	fname = BASENAME
	if TYPE[0:2] == "sm":
		fname += "-small"
		if len(TYPE) > 2:
			fname += "-attempt" + TYPE[2:]
	elif TYPE == "la":
		fname += "-large"

	f = open(fname + ".in", "r")
	lines = map(lambda x: x[:-1], f.readlines())
	f.close()
	
	outf = open(fname + ".out", "w")
	timebefore = time.time()
	main()
	timeafter = time.time()
	outf.close()
	
	runtime = timeafter - timebefore
	print "%% Runtime: %dm%2.3fs" % (int(runtime / 60), runtime % 60)
	