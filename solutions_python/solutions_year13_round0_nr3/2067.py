from math import sqrt
def palin(x):
	flag=True
	for i in range(len(x)):
		if x[i]!=x[len(x)-i-1]:
			flag=False
			break
	return flag
def fns(a,b):
	count=0
	for i in range(a,b+1):
		x=sqrt(i)
		if int(x)*int(x)==i:
			if palin(str(x)[:-2]) and palin(str(i)):
				count+=1
	return count

inp = file('input.txt','r')
output = file('output.txt','w')
t=eval(inp.readline())
for i in range(t):
	ab=inp.readline().split()
	a=eval(ab[0])
	b=eval(ab[1])
	output.write('Case #'+str(i+1)+": "+str(fns(a,b))+'\n')
