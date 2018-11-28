def valid(a):
	for i in range(len(a)-1):
		if a[i]>a[i+1]:
			return False
	return True
f1=open("B-large.in",'r')
f2=open('outputB.txt','w')
n=int(f1.readline())
for _ in range(n):
	t=list(map(int,list(f1.readline())[:-1]))
	while not valid(t):
		i=0
		while i<len(t)-1:
			if t[i]<=t[i+1]:
				i+=1
			else:
				t[i]-=1
				i+=1
				while i<len(t):
					t[i]=9
					i+=1
	s=""
	for i in t:
		if i!=0:
			s+=str(i)
	print("Case #%d: %s"%(_+1,s),file=f2)

