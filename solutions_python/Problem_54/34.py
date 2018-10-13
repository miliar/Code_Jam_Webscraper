def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

T=input()
for i in range(T):
	cin=map(long,raw_input().split())
	n=cin[0]
	a=cin[1:]
	ans=0
	a.sort()
	for j in range(n-1):
		ans=gcd(ans,a[j+1]-a[j])
	print ("Case #%d:" % (i+1)),(ans-a[0]%ans)%ans