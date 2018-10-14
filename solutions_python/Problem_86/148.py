from math import ceil
fin=open("input.txt","r")
fout=open("output.txt","w")

def gcd(a,b):
	while b:
		a,b = b,a%b
	return a
def gcd1(a):
	if not a:
		return -1
	cur=a[0]
	for i in a:
		cur = gcd(cur, i)
	return cur
def lcm(a,b):
	return a*b/gcd(a,b)
def lcm1(a):
	cur=1
	for i in a:
		cur = lcm(cur, i)
	return cur
def div(x):
	#print x
	d=[]
	i=0
	while i*i <= x:
		i += 1
		if x%i == 0:
			d += [i,x/i]
	return d
	
def get(l, h, lc, gc):
	if lc == gc:
		if lc >= l and lc <= h:
			return lc
		return 10**40
	d = sorted(div(gc))
	for i in d:
		if i >= l and i <= h and i % lc == 0:
			return i
	return 10**40
def solve():
	mn=10**40
	n,l,h = [int(i) for i in fin.readline().split()]
	a=sorted([int(i) for i in fin.readline().split()])
	for i in range(len(a)):
		#print>>fout, a[:i], a[i:]
		#print>>fout, lcm1(a[:i]), gcd1(a[i:])
		mn=min(mn, get(l,h,lcm1(a[:i]), gcd1(a[i:])))
	t=lcm1(a)
	mul = ceil(float(l) / float(t)) * t;
	if mul >= l and mul <= h:
		mn = min(mn, int(mul))
	if mn == 10**40:
		print>>fout,"NO"
	else:
		print>>fout,mn
	
t=fin.readline()
for i in range(1,int(t)+1):
	print>>fout,"Case #"+str(i)+":",
	solve()
	
