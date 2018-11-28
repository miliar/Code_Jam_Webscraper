def an(x):
	y=len(str(x))
	for l in range(0,y):
		while chkl(int(x/10**l)) is False:
			x-=10**l
			if str(int(x/10**l))[len(str(int(x/10**l)))-1]=='9':
				break
	return x

def chkl(x):
	x=str(x)
	x1=[]
	for i in range(0,len(x)):
	   	x1.append(int(x[i]))
	x1=sorted(x1)
	x2=0
	for j in range(0,len(x)):
		x2=10*x2+x1[j]
	return bool(str(x2)==x)

file1 = open("B-large.in","r")
file2 = open("result.txt","w")
n=list(file1)
for k in range(1,int(n[0])+1):
	x=int(n[k])
	while chkl(x) is False:
		x=an(x)
	file2.write('Case #')
	file2.write(str(k))
	file2.write(': ')
	file2.write(str(x))
	file2.write('\n')