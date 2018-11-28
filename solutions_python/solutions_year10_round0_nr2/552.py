from fractions import gcd
c=int(input())
for x in range(1, c+1):
	t=list(map(int, input().split()))
	n=t[0]
	del t[0]
	T=0
	for i in range(n-1):
		for j in range(i+1, n):
			T=gcd(T, abs(t[i]-t[j]))
	print('Case #' + str(x) + ': ' + str((t[0]+T-1)//T*T-t[0]))