inf = open('b-large.in', 'r')
outf = open('testAns.txt', 'w')

def finded(A, B, C):
	if A*C >= B:
		return 0
	else:
		return (finded(((A*B)**(1/2.0))/1, B, C)+1)

T = int(inf.readline())
for i in xrange(T):
	c = inf.readline()
	c = map(int, c.split())
	L = c[0]
	P = c[1]
	X = c[2]
	ans = finded(L,P,X)
	outf.write('Case #' + str(i+1) + ': ' + str(ans) + '\n')

inf.close()
outf.close()