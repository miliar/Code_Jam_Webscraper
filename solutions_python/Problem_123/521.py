
def need(a,b,c):
	ret = 0
	if (a == 1):
		return (c,-1)
	while (a <= b):
		a += a - 1
		ret+=1
	return (a,ret)

def go():
	(C,n)=map(int,raw_input().split())
	a=map(int,raw_input().split())

	a.sort()
	ret = 0
	cur = 0
	for i in xrange(0,n):
		(cur,cnt)= need(C, a[i],cur)
		if (cnt == -1):
			ret += n - i
			break;
		if (cnt < n - i):
			ret += cnt;
			C = cur;
			C += a[i];
		else:
			ret += n - i
			break
	return ret;
tn=int(raw_input())
for ts in xrange(1,tn+1):
	print "Case #%d: %d" % (ts,go())
