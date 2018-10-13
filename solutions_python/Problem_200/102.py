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
	list=[]
	for i in range(len(l[0])):
		list+=[int(l[0][i])]
	while True:
		s9=False
		for i in range(len(list)):
			#print(list,s9)
			if s9:
				list[i]=9
				continue
			try:
				if list[i]>list[i+1]:
					list[i]-=1
					s9=True
			except IndexError:
				pass 
		if s9==False:
			break
	s0=True
	for i in list:
		if i!=0:
			s0=False
		else:
			if s0:
				continue
		string+=str(i)
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