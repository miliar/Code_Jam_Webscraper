def search(eng,q):
	t=test(eng,q)
	if t:
		return 0
	max=0
	for k in eng:
		a = q.index(k)
		if max < a:
			max = a
		
	return 1 + search(eng,q[max:])

def test(a,b):
	z=0
	for k in a:
		if k not in b:
			z+=1
	return z>0


f = open('/home/jake/Desktop/A-small.in','r')
o = open('/home/jake/Desktop/A-small.out','w')
N=f.readline()
for k in xrange(0,int(N)):
    S=[]
    q=[]
    for l in xrange(0,int(f.readline())):
        S+=[f.readline()]
    for m in xrange(0,int(f.readline())):
        q+=[f.readline()]
    ans=search(S,q)
    o.write('Case #'+str(k+1)+': '+str(ans)+'\n')
f.close()
o.close()
