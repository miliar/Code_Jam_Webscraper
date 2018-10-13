n=int(input())
for i in range(n):
	s,k=input().split()
	k=int(k)
	s=s.replace('-','1').replace('+','0')
	s=int(s,2)
	ans=0
	x=int('1'*k,2)
	while s:
		ss=len(bin(s))-2
		if ss-k < 0:
			ans="IMPOSSIBLE"
			break
		s^=x<<(ss-k)
		ans+=1
	print("Case #%d: %s"%(i+1,str(ans)))