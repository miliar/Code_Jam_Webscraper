import sys
f = open(sys.argv[1], 'r')
g=open('output', 'w' )
T=int(f.readline())

def solve(g1,g2,c1,c2):
	t1=c1[g1-1]
	t2=c2[g2-1]
	s=[]
	for i in range(4):
		if(t2.count(t1[i])>0):
			s.append(t1[i])
	if(len(s)==0):
		return("Volunteer cheated! \n")
	elif(len(s)==1):
		return(str(s[0])+"\n")
	else:
		return("Bad magician! \n")
	print("\n")

for k in range(T):
	g1=int(f.readline())
	c1=[]
	for i in range(4):
		c1=c1+[[]]		
		s=f.readline()+" "
		p=0 	
		for j in range(len(s)):
			if(s[j]==' '):
				c1[i]=c1[i]+[int(s[p:j])]
				p=j+1
	g2=int(f.readline())	
	c2=[]
	for i in range(4):
		c2=c2+[[]]		
		s=f.readline()+" "
		p=0 	
		for j in range(len(s)):
			if(s[j]==' '):
				c2[i]=c2[i]+[int(s[p:j])]
				p=j+1
	g.write("Case #"+str(k+1)+": "+solve(g1,g2,c1,c2))

