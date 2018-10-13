f=open("codejam/C-large-1.in","r")
o=open("codejam/C-large-1.out","w")

count=int(f.readline())
lines = f.readlines()
j=0

def sqpal(n):
	s=str(n)
	m=len(s)
	l=int(m/2)
	for x in xrange(0, l):
		if s[x]!=s[m-x-1]:
			return False
			
	s=str(n*n)
	m=len(s)
	l=int(m/2)
	for x in xrange(0, l):
		if s[x]!=s[m-x-1]:
			return False
	return True

sqp=[]
for x in xrange(1, 10**7):
	if sqpal(x):
		sqp+=[x*x]

for line in lines:
	j+=1
	c=0
	(a,b)=tuple(int(i) for i in line.split())
	for s in sqp:
		if a<=s<=b:c+=1
	o.write("Case #%d: %d\n" % (j, c))
	
f.close()
o.close()

