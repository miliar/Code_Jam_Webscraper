def tostr(e):
	r = "["
	for c in e:
		r += "%s, " % c
	if len(e)>0:
		r = r[:-2]
	r += "]"
	return r

T = input()
for t in range(T):
	line = raw_input().split()
	line.reverse()
	C = int(line.pop())
	comb = {}
	for c in range(C):
		a = line.pop()
		comb[(a[0],a[1])]=comb[(a[1],a[0])]=a[2]
	D = int(line.pop())
	dele = set()
	for d in range(D):
		a = line.pop()
		dele.add((a[0],a[1]))
		dele.add((a[1],a[0]))
	N = int(line.pop())
	base = line.pop()
	elem = []
	for c in base:
		elem += [c]
		if len(elem)>=2 and (elem[-1],elem[-2]) in comb:
			elem = elem[:-2] + [comb[(elem[-1],elem[-2])]]
		else:
			for a in elem[:-1]:
				if (a,elem[-1]) in dele:
					elem = []
					break
	print "Case #%s: %s" % (t+1,tostr(elem))
	