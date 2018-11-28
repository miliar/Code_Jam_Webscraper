import sys	
def f(a, i):
	if a <= i: return 0
	div, mod = divmod(a,i)
	if mod == 0:
		return div - 1
	return div
	
def BBB(P):
	n = max(P)
	A = n
	for i in xrange(1,n):
		A = min(A, i + sum(map(lambda x:f(x,i),P)))
	return A

T = int(sys.stdin.readline())

for i in xrange(T):
	D = int(sys.stdin.readline())
	P = map(int, sys.stdin.readline().split())
	print "Case #%s: %s"%(i+1,BBB(P[:]))
	
