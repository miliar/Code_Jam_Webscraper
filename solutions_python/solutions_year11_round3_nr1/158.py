# Mac OS X 10.6.7 2011 MacBook Pro, pypy 1.5.0-alpha0 GCC 4.0.1
# Python 2.7.1 measured 250946 pystones/sec
import time, sys, re, math, multiprocessing
if len(sys.argv) > 1:
	inData = open(sys.argv[1]).read().strip()
else:
	inData = """3
2 3
###
###
1 1
.
4 5
.##..
.####
.####
.##..
0 0
##...
##.##
##.#.
.#.##"""
	

def parseLine(x, c):
	print "Case #"+str(c+1)+":"
	x = x[1:]
	state = [False] * len(x[0])
	buf = []
	for i in x:
		bufL = ""
		next = False
		for k,c in enumerate(i):
			if c == "#":
				state[k] = not state[k]
				if state[k] and not next:
					bufL += "/"
					next = True
				elif state[k] and next:
					bufL += "\\"
					next = False
				elif not state[k] and not next:
					bufL += "\\"
					next = True
				else:
					bufL += "/"
					next = False
			elif c == ".":
				if next:
					bufL = "Impossible"
					break
				else:
					bufL += "."
		if next:
			bufL = "Impossible"
		buf.append(bufL)
	if "Impossible" in buf:
		print "Impossible"
	elif True in state:
		print "Impossible"
	else:
		print "\n".join(buf)
if __name__ == "__main__":
	inData = inData.split("\n")
	nextIn = []
	c = 0
	for i in inData[1:]:
		if re.match("^[0-9]+ [0-9]+$", i):
			if len(nextIn) > 0:
				parseLine(nextIn, c)
				c += 1
				nextIn = []
			nextIn.append(i)
		else:
			nextIn.append(i)
	if len(nextIn) > 0:
		parseLine(nextIn, c)