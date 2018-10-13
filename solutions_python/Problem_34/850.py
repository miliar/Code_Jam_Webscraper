def flatten(a):
	for x in a:
		if type(x) in [list,tuple]:
			for i in flatten(x):
				yield i
		else:
			yield x
			
def binary_search(a,n,l=0,r=-1):
	"""performs binary search of string n on list a. l and r are the left and
         right boundaries for search"""
	if r==-1:
		r=len(a)-1
	if l>r or n<a[l] and not a[l].startswith(n) or n>a[r] and not a[l].startswith(n):
		return False
	m=(l+r)/2
	if a[m].startswith(n):
		return True
	if a[m]<n:
		return binary_search(a,n,m+1,r)
	else:
		return binary_search(a,n,l,m-1)

def prefix_exists(s):
	if expandable(s):
		prefix=s[:s.index("(")]
		if prefix=="":
			return True
		return binary_search(D,prefix)
	else:
		return binary_search(D,s)
				
def expandable(s):
	return s.count("(")>0 and s.count(")")>0

def expand(s):
	prev,v,rest=s[:s.index("(")],list(s[s.index("(")+1:s.index(")")]),s[s.index(")"):]
	if len(rest)==1:
		rest=""
	else:
		rest=rest[1:]
	p=[]
	for a in v:
		newval=prev+a+rest
		if prefix_exists(newval):
			p.append(newval)
	return p
	

def process(s):
	p=[s]
	i=0
	while True:
		"print p, p[i]"
		if prefix_exists(p[i]):
			if expandable(p[i]):
				p[i]=expand(p[i])
				p=list(flatten(p))
			else:
				i+=1
		else:
			del p[i]
		if i==len(p):
			return p
		
				

f=open("/Users/shravana/Desktop/input.txt","r")
out=open("/Users/shravana/Desktop/output.txt","w")
l,d,n=map(lambda x:int(x),list(f.readline()[:-1].split(' ')))
D=[]
for i in range(d):
	D.append(f.readline()[:-1])
D=sorted(D)

for i in range(1,n+1):
	input=f.readline()[:-1]
	output=0
	p=process(input)
	for s in p:
		if s in D:
			output+=1
	print len(p),output
	out.write("Case #%d: %d\n"%(i,output))
out.close()
del f