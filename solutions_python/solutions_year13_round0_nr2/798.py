
def comp(lawn, expt, n, m):
	for i in xrange(n):
		for j in xrange(m):
			if lawn[i][j]!=expt[i][j]:
				return 'NO'
	return 'YES'

def getAns(lawn, expt, n, m):		
	for i in xrange(n):
		h=reduce(max, expt[i])
		for j in xrange(m):
			lawn[i][j]=min(lawn[i][j], h)
				
	for j in xrange(m):
		h=0
		for i in xrange(n):
			h=max(h, expt[i][j])
		for i in xrange(n):
			lawn[i][j]=min(lawn[i][j], h)
	
	return comp(lawn, expt, n, m)
	
def foo():
	t = input()
	for n in xrange(t):
		x, y = map(int, raw_input().split())
		expt=[[] for i in xrange(x)]
		for i in xrange(x):
			expt[i]=map(int, raw_input().split())
		init=[[100 for i in xrange(y)] for j in xrange(x)]
		#print expt
		#print init
		ans = getAns(init, expt, x, y)
		print 'Case #%d: %s' % (n+1, ans)
		#return
	
if __name__ == '__main__':
	foo()


