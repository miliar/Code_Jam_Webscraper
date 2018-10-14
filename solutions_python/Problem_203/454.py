

def mainf(l,m,n):
	s=""
	l=l[1:]
	for i in range (len(l)):
		l[i]=str(l[i][0])
	ll=len(l)
	sl=[]
	for i in range(ll):
		allq=True
		for j in l[i]:
			if j!='?':
				allq=False
		if allq:
			sl+=[0]
			continue
		temp=""
		prc=0
		cprc=True
		ass='?'
		for j in range(len(l[i])):
			if l[i][j]=="?":
				if cprc==True:
					prc+=1
				else:
					temp+=ass
			else:
				if cprc==True:
					cprc=l[i][j]
				temp+=l[i][j]
				ass=l[i][j]
		pre=prc*cprc+temp
		sl+=[pre]
	for i in range(len(sl)):
		if sl[i]==0:
			mo=True
			for j in range(len(sl)):
				if j>i and sl[j]!=0:
					sl[i]=sl[j]
					mo=False
					break
			if mo:
				for j in range(len(sl)):
					if len(sl)-j-1<i and sl[-j-1]!=0:
						sl[i]=sl[-j-1]
						break
		s+="\n"+sl[i]
	
	
	

	return s

	

#main

string=""
def itxt (headlinenum=0, txt='in.txt'):
	intxt = open(txt,'r')
	returnlist=[]
	title=[]
	for i in intxt:  
		returnlist+=[str.split(i)]
	intxt.close()
	return returnlist[:headlinenum],returnlist[headlinenum:]
def otxt (s='',txt='out.txt',append='a',prt=False):
	outtxt=open(txt,append)
	outtxt.write(s)
	if prt:
		print(s)
title,l=itxt(1,'in.txt')
try:
	TC=int(title[0][0])
except ValueError:
	TC=int(title[0])
tc=0
i=0
while tc<TC:
	string+="Case #"+str(tc+1)+": "
	m=l[i][0]
	m2=l[i][1]
	m=int(m)
	m2=int(m2)
	string+=mainf(l[i:i+m+1],m,m2)+'\n'
	tc=tc+1
	i=i+m+1
otxt(string,'out.txt','w')
