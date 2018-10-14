import sys

def dbg(s): pass #sys.stderr.write(str(s))
def dbgn(s): pass #dbg(str(s) + "\n")

def read(t): return t(raw_input())
def reads(t): return map(t, raw_input().split(" "))


def gentrip(ti):
	d = ti / 3
	dm = ti % 3
	
	if dm == 2:
		return [d, d+1, d+1]
	if dm == 1:
		return [d, d, d+1]
		
	return [d, d, d]


def correct(trp, p):

	m = max(trp)
	if m >= p:
		return trp
	
	trp.sort()
	
	t2 = list(trp)
	t2[2] += 1
	t2[1] -= 1
	
	if t2[1] < 0:
		return None
	
	m = max(t2)
	
	if m - min(t2) <= 2:
		if m >= p:
			return t2
		else:
			return correct(t2, p)
	
	return None

C = read(int)

for c in xrange(1, C+1):
	l = reads(int)
	N = l[0]
	S = l[1]
	p = l[2]
	t = l[3:]
	
	dbgn("Case %d" % (c) )
	dbgn(S)
	dbgn(p)
	
	triples = []
	
	for ti in t:
		trp = gentrip(ti)
		dbg(ti)
		dbg("  ")
		dbg(trp)
		dbgn(sum(trp))
		
		triples.append(trp)
		
	triples.sort(cmp= lambda x, y:  max(y) - max(x))
	
	dbgn(triples)
	
	
	gpno = 0
	
	for trp in triples:
		m = max(trp)

		if m >= p:
			gpno += 1
			
		else:
			if S > 0:
				crt = correct(trp, p)
				
				if crt:
					gpno += 1
					if max(crt) - min(crt) > 1:
						S -= 1
	
	print "Case #%d: %d" % (c, gpno)
