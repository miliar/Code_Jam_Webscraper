import sys

def test(N,K):
	t = 0
	for i in range(N):
		t += ((K>>i) % 2)
	if t == N:
		return True
	return False

def testall(testf):
	numtests = int(testf.readline())
	for testnum in range(numtests):
		N,K = testf.readline().split()
		N = int(N)
		K = int(K)
		if test(N,K):
			good = "ON"
		else:
			good = "OFF"
		print "Case #%s: %s" % ((testnum+1),good)

fname = sys.argv[1]
f = open(fname)
testall(f)
f.close()
