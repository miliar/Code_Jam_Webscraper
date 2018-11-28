import math
linestring = open('num', 'r').readlines()
f = open('my','w')
T=int(linestring[0])
a=1

for c in (range(T)):
	bla=linestring[a].split()
	A=bla[0]
	B=int(bla[1])
	print A
	print B
	l=[]
	count=0
	i=int(A)
	while (i<B+1):
		if (str(i)==str(i)[::-1]):
			l.append(str(i))
		int(i)
		i+=1

	for j in range(len(l)):
		x=math.sqrt(int(l[j]))
	
		if(x-int(x)==0):
			if (str(int(x))==str(int(x))[::-1]):
				count+=1

	a+=1
	f.write('Case #{}: {}'.format(c+1,count)+'\n')
