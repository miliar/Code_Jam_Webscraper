import math

def SnapperChain(N,K):
	if not K:
		return 'OFF'
	b = int(math.pow(2,N))
	if K % b == (b-1):
		return 'ON'
	else:
		return 'OFF'

def testCase(fname):
	fin = open('%s.in' % fname, 'r')
	fout = open('%s.out' % fname, 'w')
	
	inread = fin.readlines()
	fin.close()
	
	x = int(inread[0])
	y = 1
	
	while x:
		N,K = inread[y].split(" ")
		fout.write('Case #%d: %s\n' % (y, SnapperChain(int(N),int(K)) ))
		y += 1
		x -= 1

testCase('A-large')