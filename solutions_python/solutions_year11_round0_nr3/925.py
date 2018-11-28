input=open("C-large.in").read().split('\n')
out=open("c.out","w")

def xor(x,y):
	return x^y

T=int(input[0].strip())
line=1
for t in xrange(1,T+1):	
	a=[int(x) for x in input[2*t].split()]
	if reduce(xor, a)==0:	
		out.write('Case #'+str(t)+': '+str(sum(a)-min(a))+'\n')
	else:
		out.write('Case #'+str(t)+': NO\n')
out.close