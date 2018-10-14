from checkfile import check
from re import findall

def checkc(com, s):
	if s=='' or len(s)==1:
		return s
	c1=com[0]
	c2=com[1]
	p=com[2]
	sa=findall('.', s)
	n=len(s)-1
	if sa[n]==c1 and sa[n-1]==c2:
		del sa[n]
		sa[n-1]=p
		s=''
		for nn in range(len(sa)):
			s+=sa[nn]
	elif sa[n]==c2 and sa[n-1]==c1:
		del sa[n]
		sa[n-1]=p
		s=''
		for nn in range(len(sa)):
			s+=sa[nn]
	else:
		pass
	return s

def checko(opp, s):
	o1=opp[0]
	o2=opp[1]
	a=s[len(s)-1]
	if a==o1:
		i=s.find(o2)
		if i==-1 or i==(len(s)-1):
			pass
		else:
			s=''
	elif a==o2:
		i=s.find(o1)
		if i==-1 or i==(len(s)-1):
			pass
		else:
			s=''
	else:
		pass
	return s
	
def cal(s):
	#variable
	final=''
	com=[]
	opp=[]
	ss=s[:-1].split(' ')
	#read-in variables
	comn=int(ss[0])
	for n in range(comn):
		com.append(ss[n+1])
	oppn=int(ss[comn+1])
	for n in range(oppn):
		opp.append(ss[n+comn+2])
	y=ss[len(ss)-1]
	
	for n in range(len(y)):
		final+=y[n]
		final2=final
		for nn in range(comn):
			final2 = checkc(com[nn], final)
		if final==final2:
			for nn in range(oppn):
				final2 = checko(opp[nn], final)
		final=final2
	#show ans
	ans='['
	for n in range(len(final)):
		ans+=final[n]
		if n!=(len(final)-1):
			ans+=', '
	ans+=']'
	return ans
#function end
	
v=0
n=''
while v==0:
	n=raw_input("Enter the name of the file: ")
	v=check(n)
	if v==0:
		print("Please insert a valid file name, enter 'quit' to exit\n")
	elif v==1:
		w=1
	elif v==2:
		w=0
if w==1:
	i=open(n+'.in', 'r')
	o=open(n+'.out', 'w')
	#main code
	loop=int(i.readline())
	count=0
	anss=[]
	output=''
	while count<loop:
		q=i.readline()
		ans=cal(q)
		anss.append(ans)
		count+=1
	#display stuff
	output=''
	for l in range(len(anss)):
		output+='Case #'+str(l+1)+': '+anss[l]
		if l!=len(anss)-1:
			output+='\n'
	print output
	o.write(output)
	#end of main code