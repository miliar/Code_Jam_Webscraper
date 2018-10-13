string=""
sym=['.','+','x','o']
ivsym={'.':0,'+':1,'x':2,'o':3}
def itxt (headlinenum=0, txt='in.txt'):
	intxt = open(txt,'r')
	returnlist=[]
	title=[]
	for i in intxt:  
		returnlist+=[str.split(i)]
	intxt.close()
	return returnlist[:headlinenum],returnlist[headlinenum:]

def fillchart (l,n):
	a=[i[0] for i in l]
	b=[i[1] for i in l]
	c=[]
	d=[]
	for i in range(n):
		if i+1 not in a:
			c+=[i+1]
		if i+1 not in b:
			d+=[i+1]
	for i in range(len(c)):
		l+=[[c[i],d[i]]]
	return l
			
def dt(i):
	if i>1:
		return i-1 
	return i
	
def mainf(l,string,m):
	onestr=''
	n=int(l[0][0])
	oc=[[0 for i in range(n)] for i in range (n)]
	pc=[[0 for i in range(n)] for i in range (n)]
	sc=[]
	it=True
	for i in l:
		if it:
			it=False 
			continue 
		a=int(i[1])
		b=int(i[2])
		if i[0] in "o+":
			pc[a-1][b-1]=1 
		if i[0] in "ox":
			sc+=[[a,b]]
		oc[a-1][b-1]=ivsym[i[0]]
	sc=fillchart(sc,n)
	pc[-1]=[1 for i in range(n)]
	pc[-1][0]=0
	pc[-1][-1]=0
	pc[0]=[1 for i in range(n)]
	for i in sc:
		pc[i[0]-1][i[1]-1]+=2
	inc=0
	chg=0
	for i in range(n):
		for j in range(n):
			tempp=pc[i][j]
			tempo=oc[i][j]
			inc+=dt(tempp)
			if tempp!=tempo:
				chg+=1
				onestr+=sym[pc[i][j]]+' '+str(i+1)+' '+str(j+1)+'\n'
	onestr=str(inc)+' '+str(chg)+'\n'+onestr
	
	
	#print(sc,pc,oc)
	
	
	
	
	string+=onestr
	string+="\n"
	return string

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#main

title,l=itxt(1,'a.txt')
try:
	TC=int(title[0][0])
except ValueError:
	TC=int(title[0])

tc=0
i=0
while tc<TC:
	string+="Case #"+str(tc+1)+": "
	m=l[i][1]
	m=int(m)
	string=mainf(l[i:i+m+1],string,m)
	tc=tc+1
	i=i+m+1
def otxt (s='',txt='out.txt',append='a',prt=False):
	outtxt=open(txt,append)
	outtxt.write(s)
	if prt:
		print(s)
otxt(string,'out.txt','w')