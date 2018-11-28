def cycle(perm):
	r=[]
	l=list(perm)
	for i in xrange(len(l)):
		if l[i]==-1: continue
		cnt=0
		p=i
		while l[p]!=-1:
			cnt+=1
			t=p
			p = l[p]
			l[t] = -1
		r.append(cnt)
	return r

def solve(cs):
	n = input()
	l = map(int,raw_input().split())
	d = {}
	l2 = sorted(l)
	for i in xrange(n):
		d[l2[i]] = i
	for i in xrange(n):
		l[i] = d[l[i]]
	r = cycle(l)
	sm = 0
	for rr in r:
		if rr>1: sm += rr
	print "Case #%d: %d" % (cs+1, sm)

t=input()
for i in xrange(t):
	solve(i)
