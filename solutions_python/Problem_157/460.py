def convert(a):
	a = a[len(a)-1]
	if a=='1':
		return 0
	elif a=='i':
		return 1
	elif a=='j':
		return 2
	elif a=='k':
		return 3

def multiplication(a,b):
	quaternions = [['1','i','j','k'],['i','-1','k','-j'],['j','-k','-1','i'],['k','j','-i','-1']]
	if len(str(a))>1 and len(str(b))>1:
		a = convert(a)
		b = convert(b)
		x =  quaternions[a][b]
	elif len(str(a))>1 or len(str(b))>1:
		a = convert(a)
		b = convert(b)
		x = '-'+quaternions[a][b]
	else:
		a = convert(a)
		b = convert(b)
		x = quaternions[a][b]
	if len(x)==3:
		return x[len(x)-1]
	else:
		return x

def dijkstra(l,x,s):
	stol = []
	s=s*x
	for x in s:
		stol.append(x)
	i=stol[0]
	while i!='i':
		if len(stol)>1:
			a = stol[0]
			b = stol[1]
			c = multiplication(a,b)
			stol[1]=c
			i=c
			stol.remove(stol[0])
		else:
			return "NO"
	j=stol[1]
	while j!='j':
		if len(stol)>2:
			a = stol[1]
			b = stol[2]
			c = multiplication(a,b)
			stol[2]=c
			j=c
			stol.remove(stol[1])
		else:
			return "NO"
	stol.remove(i)
	stol.remove(j)
	k = stol[0]
	stol.remove(stol[0])
	for x in xrange(len(stol)):
		k = multiplication(k,stol[0])
		stol.remove(stol[0])
	if k=='k':
		return "YES"
	else:
		return "NO"

def read_and_write(readfrom,writein):
	inp = open(readfrom,'r')
	outp = open(writein, 'w')
	test = int(inp.readline().split(' ')[0])
	for i in xrange(test):
		a = map(int,inp.readline().split())
		b = inp.readline()
		b = b[:len(b)-1]
		c = dijkstra(a[0],a[1],b)
		outp.write("Case #%d: %s\n"%(i+1,c))
	inp.close()
	outp.close()

execute=raw_input("Test, small or large?: ")
read = "C-%s-attempt0.in"%(execute)
write = "C-%s-output.txt"%(execute)

read_and_write(read,write)