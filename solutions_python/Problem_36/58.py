
import sys

def readstr():
	return sys.stdin.readline().strip()

def readint():
	return int(readstr())

N = readint()

target = "welcome to code jam"
rev = target[::-1]
m = 10000
l = 4

for i in range(N):
	s = readstr()
	n = len(s)
	
	ol = [1]*(n+1)


	for c in rev:
		ne = [0]*(n+1)
		cur = 0
		for j in xrange(n):
			if s[-(j+1)] == c:
				cur = ( cur + ol[n-j] ) % m
			ne[n-j-1]  = cur
		ol = ne

	ans = str( ne[0] )
	if len(ans) < l:
		ans = '0' * (l-len(ans)) + ans

	print "Case #"+str(i+1)+": "+ans


