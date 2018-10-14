#AdiX
import math
testcase = int ( input() )

for itestcase in range(0,testcase):
	count = 0;
	x=0
	a=[]
	b=[]
	n=int(input())

	
	for i in range(0,n):
		q,w=input().split(" ")
		a.append(q)
		b.append(w)

	for j in range(0,n):
		for k in range (j+1,n):
			if((int(a[j])<int(a[k]) and int(b[j])>int(b[k])) or (int(a[j])>int(a[k]) and int(b[j])<int(b[k]))):
				count=count+1
		
	print("Case #"+str(itestcase+1)+": "+str(count))
