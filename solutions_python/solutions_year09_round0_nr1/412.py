FI = 'A-large.in'
#FI="in"

dict = {}

def add(word):
	global dict
	ptr = dict
	while word != "":
		if word[0] not in ptr: ptr[word[0]] = {}
		ptr = ptr[word[0]]
		word = word[1:]

def cnt(ptr, suffix):
	if suffix == "":
		return 1
	elif suffix[0] == "(":
		sum = 0
		cands = suffix[1:suffix.find(")")]
		rest = suffix[suffix.find(")")+1:]
		for c in cands:
			if c in ptr:
				sum += cnt(ptr[c], rest)
		return sum
	elif suffix[0] in ptr:
		return cnt(ptr[suffix[0]], suffix[1:])
	else:
		return 0
		
def case(fi, fo, n, si):
	s = fi.readline().strip()
	s = s.replace("(","[").replace(")","]")
	si.write('echo -n "Case #%d: "\n' % n)
	si.write('egrep -c "%s" dict.txt\n' % s)

# ---

def rl(f, n):
	return [f.readline() for i in xrange(n)]
def zw(fs, es):
	return [f(e) for f,e in zip(fs, es)]
def cases(fi, fo):
	L,D,N = zw([int,int,int], fi.readline().split())
	di = open("dict.txt", "w")
	for s in rl(fi, D):
		di.write("%s" % s)
	di.close()
	si = open("script.sh", "w")
	for i in xrange(N):
		case(fi, fo, i+1, si)

fi = open(FI)
fo = open('out.txt', 'w')
cases(fi, fo)
fi.close()
fo.close()

f = open('out.txt')
print f.read()
