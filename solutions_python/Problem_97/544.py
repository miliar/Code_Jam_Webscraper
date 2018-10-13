import sys,os,itertools
from math import log10
import cPickle

def getline():
	return sys.stdin.readline().rstrip()

def digits(n):
	d = 0
	step = 1
	while step <= n:
		d += 1
		step *= 10
	return max(1, digits)


def dcnt(i,j):
	if sum(map(int, str(i))) != sum(map(int, str(j))): return False
	d1 = sorted([ int(x) for x in str(i) ])
	d2 = sorted([ int(x) for x in str(j) ])
	for i in range(len(d1)):
		if d1[i] != d2[i]: return False
	return True

T = int(getline())

def check(n, A, B, done):
	if n < 10: return 0
	cnt = 0
	d = [ int(x) for x in str(n) ]
	for i in range(1,len(d)):
		if d[i] == 0: continue
		x = 0
		m = True
		d1 = d[i:]
		d2 = d[:i]
		if d1 == d2: continue
		for j in d1:
			x = x*10+j
			if x > B: 
				m = False
				break
		if not m: continue
		for j in d2:
			x = x*10+j
			if x > B: 
				m = False
				break
		if m and x!=n and x >= A and x <= B: 
			pair = x > n and (x,n) or (n,x)
			if not pair in done:
				done.add(pair)
				cnt += 1
	return cnt
CACHE_FILE = "C.data"
if not os.path.exists(CACHE_FILE):
	print >>sys.stderr,"Generating dataset cache..."
	A,B = 1,2000001
	r = range(A, B)
	data = set()
	for n in r: check(n, A, B, data)
	cached = dict()
	for x,y in data:
		if not x in cached: cached[x] = [y]
		else: 
			l = cached[x]
			l.append(y)
			l.sort()
	cached = sorted(cached.iteritems())

	print >>sys.stderr,"Creating partitions..."
	partitions = dict()
	for i in range(21): partitions[100000*i]=[]
	for el in cached:
		i = el[0]
		partitions[i-i%100000].append(el)

	cached = sorted(partitions.iteritems())

	for pk,el in cached:
		print pk,"->",len(el)

	print >>sys.stderr,"Writing dataset to file..."
	f = open(CACHE_FILE,'wb')
	cPickle.dump(cached, f)
	f.close()
else:
	print >>sys.stderr,"Loading dataset ..."
	f = open(CACHE_FILE,'rb')
	cached = cPickle.load(f)
print >>sys.stderr,"Dataset contains %d elements" % len(cached)
 
for case in range(1,T+1):
	A,B = [ int(x) for x in getline().split() ]
	r = range(A,B+1)
	res = 0
	first = A-A%100000
	for off,part in cached:
		if off < first: continue
		if B < off: break
		for x,ys in part:
			if x < A: continue
			if x > B: break
			for y in ys: 
				if y < A: continue
				if y > B: break
				res += 1
	print "Case #%d: %d" % (case, res)
