import sys

def mainCase(valC):
	N,K = map(int,valC.rstrip().split(" "))
	S = [0] * N
	ON = 0
	for i in xrange(K):
		ON = 1
		for j in xrange(len(S)):
			if S[j] == 0:
				S[j] = 1
				break
			else:
				S[j] = 0
			
	for v in S:
		if v == 0 : return "OFF"
	return "ON"
	
	
fname = "/Users/fopina/Downloads/A-small-attempt0.in"
#fname = "t.in"

f = open(fname,"r")
tnr = int(f.readline())

for i in xrange(1,tnr+1):
	print "Case #" + str(i) + ": " + mainCase(f.readline())
