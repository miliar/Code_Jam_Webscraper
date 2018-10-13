ans=''
for test in range(int(input())):
	d,n=[ int(x) for x in input().split()]
	l=[]
	m=10**10
	for i in range(n):
		t=[ int(x) for x in input().split()]
		l.append(t)
		di=(t[0]-d)/t[1]
		if di<m:
			m=di
	t="{0:.6f}".format(-d/m)
	ans+="Case #"+str(test+1)+": "+t+"\n"
print(ans[:-1])

