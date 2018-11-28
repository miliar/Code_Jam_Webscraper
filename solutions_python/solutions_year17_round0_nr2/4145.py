l=0
org="B-large (1).in"
inp=open(org,'r')
t= int(inp.readline())
lines=inp.readlines()
#print lines
wfilename="output.txt"
dest=open(wfilename,'w')
def posTidy(num):
	i=1
	pos=-1
	tmp=num
	dig=tmp%10
	tmp=int(tmp/10)
	while(tmp>0):
		if((tmp%10)>dig):
			pos=i
		if(num==884):
			print k
		dig=tmp%10
		tmp=int(tmp/10)
		i+=1
	return pos
while (l<t):
	num=int(lines[l])
	j=0
	res=0
	td=-1
	p=1
	k=posTidy(num)
	if(k==-1):
		res=num
	else:
		while(num>0):
			dig=num%10
			if(j<k):
				res=9*p+res
			if(j==k):
				if(dig==int(num/10)%10):
					k+=1
					res=9*p+res
				else:		
					res=(dig-1)*p+res
			if(j>k):
				if(dig==td):
					res=9*p+res
				else:
					res=dig*p+res
			j+=1
			num=int(num/10)
			p=p*10	
	l+=1
	line="Case #"+str(l)+": "+str(res)             	
	dest.write(line)
	dest.write("\n")
dest.close()