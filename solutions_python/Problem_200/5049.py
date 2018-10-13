i=0
org="B-small-attempt0.in"
inp=open(org,'r')
t= int(inp.readline())
lines=inp.readlines()
#print lines
wfilename="output.txt"
dest=open(wfilename,'w')
def isTidy(num):
	dig=num%10
	num=int(num/10)
	while(num>0):
		if((num%10)>dig):
			return False
		else:
			dig=num%10
		num=int(num/10)
	return True
while (i<t):
	num=int(lines[i])
	while(num>0):
		if(isTidy(num)):
			break
		else:
			num-=1	
	i+=1
	line="Case #"+str(i)+": "+str(num)             	
	dest.write(line)
	dest.write("\n")
dest.close()

