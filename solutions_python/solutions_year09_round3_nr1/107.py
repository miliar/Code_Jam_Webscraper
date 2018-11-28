import sys

def solve(vec):
	num=map(lambda x:0,range(len(vec)))
	b={}
	v={}
	v[vec[0]]=1
	i=0
	while  i<len(vec) and vec[i] == vec[0]:
		i+=1
	if i<len(vec):
		v[vec[i]]=0
	x=2
	c=0
	for i in vec:
		b[i]=1
		if v.has_key(i):
			num[c]=v[i]
		else:
			v[i]=x
			num[c]=x
			x+=1
		c+=1
	base=len(b)
	if base==1:
		base=2
	m=1
	ret=0
	for j in xrange(len(vec)):
		ret=ret+num[len(vec)-j-1]*m
		m=m*base
	return ret

			
def readVector(f):
	vec=[]
	string=f.readline()
	for x in xrange(len(string)):
		if ord('a') <= ord(string[x]) <= ord('z') or ord('0') <= ord(string[x]) <= ord('9'):
			vec.append(string[x])
	return vec
	
def main():
	if len(sys.argv)!=3:
		raise Exception('You should pass names of input and output files')	
	f=open(sys.argv[1])
	r=open(sys.argv[2],'w')
	t=int(f.readline())	
	for i in xrange(t):
		vec=readVector(f)
		sec=solve(vec)
		r.write('Case #%d: %d\n' % (i+1, sec))
	f.close()
	r.close()
	
main()