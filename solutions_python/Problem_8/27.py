import os
# requires the gnu factor program

def fit(x, p):
	if x <= 1: return set([])
	return set(int(y) for y in (os.popen("factor %s"%x).read().split(': ')[1]).split(' ') if int(y) >= p)

def doit(fed):
	for i in range(len(fed)):
		for j in range(len(fed)):
			if i != j:
				if(len(fed[i].intersection(fed[j])) > 0):
					fed[i] = fed[i].union(fed[j])
					fed.remove(fed[j])
					return 0
	return 1

def case():
	x, y, p = (int(i) for i in raw_input().split(' '))
	fed = [fit(x, p) for x in range(x, y + 1)]
	tot = len(fed)
	fed = [x for x in fed if len(x) > 0]
	done = 0
	while not doit(fed): pass
	print len(fed)

ncases = int(raw_input())
for i in range(ncases):
	print "Case #" + str(i+1) + ":",
	case()
