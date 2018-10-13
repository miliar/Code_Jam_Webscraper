T = int(raw_input())
#n = "987654321"
for t in xrange(T):
	n = raw_input()
	nl = [x for x in n]
	nxt = n
	i = 1
	changed = False
	for i in xrange(len(n)-1, 0, -1):
		if n[i-1] < n[i]:
			m = nl[:]
			tmp = m[i]
			tmpi = i
			for j in xrange(i, len(m)):
				if (m[j] < tmp) and (m[j] > nl[i-1]):
					tmp = m[j]
					tmpi = j
			m[i-1], m[tmpi] = m[tmpi], m[i-1]
			a = m[i:]
			a.sort()
			m[i:] = a
			nxt = "".join(m)
			changed = True
			break
	if (changed==False):
		nl.sort()
		cnt = 1
		while nl[0] == "0":
			nl.pop(0)
			cnt+=1
		m = [nl[0]]+["0"]*cnt+nl[1:]
		nxt = "".join(m)
	print "Case #%d: %s" % (t+1, nxt)

