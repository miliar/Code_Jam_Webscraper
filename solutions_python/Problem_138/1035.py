#war.py - Python 3.2.1

from sys import argv

def popgreater(lis,value):
	z=-1
	for k,l in enumerate(lis):
		if(l>value): z=k; break
	
	return lis.pop(z) if z>=0 else -1

with open(argv[1]) as fin, open(argv[1].replace(".in",".out"),'w') as fout:
	T=int(fin.readline())
	for Tt in range(1,T+1):
		N=int(fin.readline())
		x=list(map(float,fin.readline().split()))
		y=list(map(float,fin.readline().split()))
		x.sort(); y.sort()
		#print(x,y)
		#War
		n1=0
		ywar=list(y)
		for i in x:
			if(popgreater(ywar,i)<0): n1+=1
		#DWar
		n2=0
		for i in range(N):
			if(x[-1]>y[-1]): 
				x.pop();y.pop();n2+=1
			else:
				x.pop(0);y.pop();
			
		
		fout.write('Case #{0}: {1} {2}\n'.format(Tt,n2,n1))
		#print(Tt,":",n2,n1)
		
