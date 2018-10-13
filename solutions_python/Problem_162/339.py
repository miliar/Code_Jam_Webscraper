import fileinput
import sys
import math

result = {1: 1}

def switch(n):
	return int(str(n)[::-1])

def getmin(n):
	global result
	if not n in result:
		if n % 10 != 0 and switch(n) < n:
			result[n] = 1 + min(getmin(n-1), getmin(switch(n)))
		else:
			result[n] = 1 + getmin(n-1)
	return result[n]

def buildres():
	for i in xrange(2,1000000):
		getmin(i)

def ex1B2(line):
	target = int(line)
	return getmin(target)

if __name__ == '__main__':
	buildres()
	ncases = int(sys.stdin.readline())
	for i in range(1, ncases + 1 ):
		print "Case #{0}: {1}".format(i, ex1B2(sys.stdin.readline().rstrip()))
    	

    	
