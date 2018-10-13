
def counthem(pos,oc):
	i = pos
	count = 0
	while i<len(oc):
		if oc[i] == 0:
			break
		count += 1
		i += 1
	i = pos-2
	while i>=0:
		if oc[i] == 0:
			break
		count += 1
		i -= 1
	return count


def resolve(p,q,oc,order):
	if q == 0:
		return 0
	count = 10000*10000
	for i in order:
		oc2 = [oc[j] for j in xrange(len(oc))]
		oc2[int(i)-1] = 0
		a = [j for j in order]
		a.remove(i)
		tmp = counthem(int(i),oc2)
		tmp += resolve(p,q-1,oc2,a)
		if tmp < count:
			count = tmp
	return count

t = int(raw_input())

for i in xrange(t):
	r = raw_input().split()
	p = int(r[0])
	q = int(r[1])

	oc = [1 for j in xrange(p)]

	order = raw_input().split()

	print "Case #"+str(i+1)+":",resolve(p,q,oc,order)
