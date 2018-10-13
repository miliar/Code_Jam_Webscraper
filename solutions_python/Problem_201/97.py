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
	n=l[0]
	k=l[1]
	n=int(n)
	k=int(k)
	d=n-k 
	while True:
		k=k//2
		if k==0:
			break 
		d=d//2
	h=d//2 
	string+=str(d-h)+' '+str(h)
	string+="\n"
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