import sys
from math import ceil, floor

filename = str(sys.argv[1])
f = open(filename,'r')

# dump first line
g = f.readline()

# Return greatest power of 2 less than K
def genP2(K):
        i = 1
        P = 0
        while 2**i <= K:
                P = 2**i
                i += 1
        return P

# represent output
def rep(l,r,case):
	print "Case #%d: %d %d" % (case,max(l,r),min(l,r))
	
		  
def main():
	caseNum = 1
	for line in f:
		line = line.strip()
		line = line.split()
		# print "input: " + str(line)
		N = int(line[0])
		K = int(line[1])
		try:
			magicNumber = (N-K) / genP2(K)
		except:
			magicNumber = (N-K) / 1.0
		L = floor(magicNumber / 2.0)
		R = ceil(magicNumber / 2.0)
		# print "magicNumber: %d" % magicNumber
		# print "magicNumber/2: %f" % (magicNumber/2)
		# print "L: %d" % L
		# print "R: %d" % R
		
		rep(L,R,caseNum)
		caseNum += 1
			

main()
