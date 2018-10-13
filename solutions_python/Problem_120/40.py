I = lambda : map(int,raw_input().split())
def check(r,t,d):
	return 2*r*d+2*d*d-d<=t

T = int(raw_input())
for ww in range(T):
	r,t=I()
	ll=0
	rr=1000000000000000000
	ans=0
	while (ll<=rr):
		mid=(ll+rr)//2;
		if (check(r,t,mid)):
			ans=mid;
			ll=mid+1;
		else:
			rr=mid-1;
	print 'Case #'+str(ww+1)+': '+str(ans)