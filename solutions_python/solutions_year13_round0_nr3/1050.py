import sys
import math

root = 0

def isPal(a):
	#print a
	b = a[::-1]
	#print b
	return not(cmp(a,b))
def isSquare(i):
	global root
	root = int(math.sqrt(i))
	#print "root = " + str(root)
	if root*root == i:
		return True
	else:
		return False

if __name__ == "__main__":
	T = int(sys.stdin.readline().strip())
	for caseno in xrange(T):
		L = sys.stdin.readline().strip().split(' ')
		L1 = map(int,L)
		result = 0
		for i in xrange(L1[0],L1[1]+1):
			if isPal(str(i)) and isSquare(i) and isPal(str(root)):
				result+=1;
		print "Case #%d: %d" % (caseno + 1, result)
