def area(r):
	return 2*r-1
def rings(r,t):
	noRings=0
	cur=r+1
	while True:
		t-=area(cur)
		if t<0:
			return noRings
		noRings+=1
		cur+=2
lines=[i.replace('\n','') for i in open('A-small-attempt0.in','r').readlines()[1:]]
out=open('output.txt','w')
for i in range(len(lines)):
	q=lines[i].split()
	r=int(q[0])
	t=int(q[1])
	out.write(('Case #{0}: '+str(rings(r,t))+'\n').format(i+1))