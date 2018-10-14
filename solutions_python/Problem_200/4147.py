def f(n):
	if n== 1:
		return 1
	for j in range(n,1,-1):
		a = "".join(sorted(str(j)))
		b = "".join(sorted(str(j), reverse =True))
		if a==str(j):
			return j
		elif b==str(j):
			j=str(j)	
			f=int(j[0])-1
			l=""
			for k in range(0,int(len(j)-1)):
				l=l+"9"
			if f==0:
				return l
			fin = str(f) + l
			return fin

t=input()
t=int(t)
for i in range(1,t+1):
	n=int(input());
	print ("Case #"+str(i)+": "+str(f(n)));