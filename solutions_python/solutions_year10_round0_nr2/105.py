

def gcd(a,b):
	if a<b:
		return gcd(b,a)
	if b==0:
		return a
	return gcd(b,a%b)

infile = file('B-large.in', 'r')
outfile = file('bout.txt', 'w')

C = int(infile.readline())

for a in range(C):
	vals=[]
	mn=-1
	vl=infile.readline()
	vr=vl.split()
	n=long(vr[0])
	vr=vr[1:]
	
	for i in vr:
		iv=long(i)
		vals.append(iv)
		if (mn == -1) or (mn > iv):
			mn=iv
	
	for i in range(n):
		vals[i]=vals[i]-mn
	
	r=vals[0]
	for i in range(n):
		r=gcd(r,vals[i])
		
	
	rv=r-(mn%r)
	if rv==r:
		rv=0
	
	outfile.write('Case #%d: ' %(a+1))
	outfile.write('%d\n' % rv)
	print rv