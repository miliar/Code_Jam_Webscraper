# Mac OS X 10.6.7 2011 MacBook Pro, pypy 1.5.0-alpha0 GCC 4.0.1
# Python 2.7.1 measured 250946 pystones/sec
import time, sys, re, math, multiprocessing
if len(sys.argv) > 1:
	inData = open(sys.argv[1]).read().strip()
else:
	inData = """2
3 2 100
3 5 7
4 8 16
1 20 5 2"""
	

def parseLine(x, c):
	print "Case #"+str(c+1)+":",
	x[0] = map(lambda x: int(x), x[0].split(" "))
	x[1] = map(lambda x: int(x), x[1].split(" "))
	for i in xrange(x[0][1], x[0][2]+1):
		ok = True
		#print "CHECK", i
		for n in x[1]:
			if i % n != 0 and n % i != 0:
				#print "FAIL at", n
				ok = False
				break
		if ok:
			print i
			return
	print "NO"

if __name__ == "__main__":
	inData = inData.split("\n")
	nextIn = []
	c = 0
	for k,i in enumerate(inData[1:]):
		if k % 2 == 0:
			nextIn.append(i)
		else:
			nextIn.append(i)
			parseLine(nextIn, c)
			c += 1
			nextIn = []
	if len(nextIn) > 0:
		parseLine(nextIn, c)