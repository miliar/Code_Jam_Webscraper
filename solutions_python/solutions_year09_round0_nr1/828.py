Code:


import re,sys

file=sys.argv[1]
input=open(file)
l=input.readline()
topline=l.split(' ')
L=topline[0]
D=topline[1]
N=topline[2]
string=""
for x in range(int(D)):
	l=input.readline()
	string=string+l.rstrip()+','
	

for x in range(int(N)):
	l=input.readline().strip()
	pattern=l.replace('(','[')
	pattern=pattern.replace(')',']')
	print ("Case #{0}:".format(x+1),end=' ') 
	#print (pattern)
	print(len(re.findall(pattern,string)))
