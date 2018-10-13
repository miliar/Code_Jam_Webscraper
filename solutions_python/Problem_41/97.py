def listOfDigits(n):
	k = n
	ret = []
	while k>0:
		k, c = divmod(k, 10)
		ret.append(c)
	return [x for x in reversed(ret)]
	
def digitsToNumber(a):
	return reduce(lambda x,y: x*10+y, a)
	
def next(a):
	if len(a)<2:
		return a
	p1 = len(a)-2
	while p1>-1 and not(a[p1]<a[p1+1]):
		p1-=1
	if p1==-1:
		return a
	else:
		p2 = len(a)-1
		while a[p2]<=a[p1]:
			p2-=1
		a[p1],a[p2] = a[p2],a[p1]
		aux = a[p1+1:]
		aux.reverse()
		a[p1+1:] = aux
		return a

lines = open("B-large.in").read().split("\n")
t = int(lines[0])
output = []
for q in xrange(1,t+1):
	n = int(lines[q])
	a = listOfDigits(n)
	a1 = a[:]
	a = next(a)
	if a==a1:
		a = [0]+sorted(a)
		k=0
		while a[k]==0:
			k+=1
		a[k],a[0] = a[0], a[k]
	output.append("Case #"+str(q)+": " + str(digitsToNumber(a)))
	#print output[-1]
	
open("results.txt","w").write("\n".join(output))