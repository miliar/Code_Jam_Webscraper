FI = 'A-large.in'
def case(fi, fo, n):
	t = int(fi.readline())
	v1 = map(int, fi.readline().split())
	v2 = map(int, fi.readline().split())
	v1.sort()
	v2.sort()
	v2.reverse()
	val = 0
	for a,b in zip(v1,v2):
		val += a*b
	fo.write('Case #%d: %d\n' % (n, val))


# ---

def rl(f, n):
	return [f.readline() for i in xrange(n)]
def zw(fs, es):
	return [f(e) for f,e in zip(fs, es)]
def cases(fi, fo):
	for i in xrange(int(fi.readline())):
		case(fi, fo, i+1)

fi = open(FI)
fo = open('out.txt', 'w')
cases(fi, fo)
fi.close()
fo.close()

f = open('out.txt')
print f.read()
