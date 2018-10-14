INF=1000000000
RANGE=1000005
def solv(ans) :
	ans[1]=1
	for i in xrange(1,RANGE-1) :
		rev=int(str(i)[::-1])
		ans[i+1]=min(ans[i+1],ans[i]+1)
		if rev<RANGE :
			ans[rev]=min(ans[rev],ans[i]+1)

ans=[INF for x in xrange(RANGE)]
solv(ans)
t=int(input())

for i in xrange(1,t+1) :
	n=int(input())
	print "Case #%d: %d"%(i,ans[n])
