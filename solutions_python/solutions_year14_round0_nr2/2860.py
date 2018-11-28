import sys
f = open(sys.argv[1], 'r')
g=open('outputtry', 'w' )
T=int(f.readline())
for i in range(T):
	s=f.readline()
	for j in range(len(s)):
		if(s[j]==' '):break
	C=float(s[:j])
	for K in range(j+1,len(s)):
		if(s[K]==' '):break
	F=float(s[j+1:K])
	X=float(s[K+1:])
	time=0.0
	n=int(X/C-2/F)
	g.write("Case #"+str(i+1)+": ")
	if(n>=0):
		time=time+(X/(2+n*F))
		for i in range(n):
			time=time+(C/(2+(n-1-i)*F))
	else:
		time=X/2
	g.write(str(time)+"\n")
