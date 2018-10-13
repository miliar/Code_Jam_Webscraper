t=int(input())
for i in range(t):
	l,N=input().split();a=s=0
	for j in range(int(l)+1):
		if s<j:a+=j-s;s=j
		s+=int(N[j])
	print("Case #"+str(i+1)+":",a)
