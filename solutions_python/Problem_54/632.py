import sys

def gcd(a,b) :
	if b > a:
		(a,b) = (b,a)
	while(b != 0):
		(a,b)= (b,a%b)
	return a

def reduce(l):
	first = l[0]
	if len(l) == 2 :
		l.append(l.pop() -first)
	while(len(l) > 2):
		a = l.pop() - first
		b = l.pop() - first
		l.append(gcd(a,b))
	return l



def process(l,i) :
	l.sort()
	l = reduce(l)
	a,b= l[0],l[1]
	r = b-a
	while(r < 0):
		r+=b
	return "Case #%d: %d" % (i,r) 
	
i = 0
for line in file(sys.argv[1]):
	if i == 0:
		i += 1
		continue
	l = map(lambda x:int(x), line.split(" "))
	
	print process(l[1:],i)
	i += 1