string=""
def itxt (headlinenum=0, txt='in.txt'):
	intxt = open(txt,'r')
	returnlist=[]
	title=[]
	for i in intxt:  
		returnlist+=[str.split(i)]
	intxt.close()
	return returnlist[:headlinenum],returnlist[headlinenum:]

def mainf(l,string):
	a=l[0]
	b=l[1]
	b=int(b)
	d=len(a)
	c=[]
	op=0
	for i in range(d):
		if a[i]=='+':
			c+=[1]
		else:
			c+=[0]
	print(c)
	for i in range(d):
		if c[i]==0:
			for j in range(b):
				try:
					c[i+j]=1-c[i+j]
				except IndexError:
					string+="IMPOSSIBLE\n"
					return string 
			op+=1 
	string+=str(op)+"\n"
	return string

#main

title,l=itxt(1,'a.txt')
try:
	TC=int(title[0][0])
except ValueError:
	TC=int(title[0])

tc=0
while tc<TC:
	string+="Case #"+str(tc+1)+": "
	string=mainf(l[tc],string)
	tc=tc+1
def otxt (s='',txt='out.txt',append='a',prt=False):
	outtxt=open(txt,append)
	outtxt.write(s)
	if prt:
		print(s)
otxt(string,'out.txt','w')