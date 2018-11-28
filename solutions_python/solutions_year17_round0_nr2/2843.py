f = open("B-large.in","r")
out = open("output.out","a")
case = int(f.readline())
def chck(x):
	y = map(int,x)
	for i in range(1,len(y)):
		if y[-i]<y[-(1+i)]:
			return 0
	return 1
o=[]

def fun(x):
	y = map(str,x)
	y.pop()
	y = ''.join(y)
	return int(y)

def lst(x,y):
	z = map(str,x)
	z.append(y*str("9"))
	z = ''.join(z)
	return int(z)

for i in range(case):
	inp = int(f.readline())
	c=0
	while(inp>0):
		if chck(str(inp)):
			break
		if inp%10 == 9:
			c+=1
			inp = fun(str(inp))	
		inp-=1
	if c!=0:
		o.append(lst(str(inp),c))
	else:
		o.append(inp)
for i in range(case):
	out.write("Case #"+str(i+1)+": "+str(o[i])+"\n")
