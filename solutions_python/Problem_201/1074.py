from sortedcontainers import *
def isodd(num):
	return num & 1 and True or False

def split(n):
	if isodd(n):
		return n/2, n/2
	else:
		return (n/2) -1 , n/2

T = int(raw_input())
for t in xrange(T):
	NK = raw_input().split()
	n, k =  int(NK[0]), int(NK[1])

	# print n, k

	q = SortedList()
	q.add(n)

	m = {n: 1}

	i = 0

	while i < k and len(q) > 0:
		
		s = q.pop()
		ls, rs = split(s)
		# print "n=", n, "q=", q,"m=", m,"i=", i, "s=", s, "ls=", ls, "rs=", rs 

		if ls:
			if ls in m:
				m[ls] += m[s]
			else:
				m[ls] = m[s]
				q.add(ls)

		if rs:
			if rs in m:
				m[rs] += m[s]
			else:
				m[rs] = m[s]
				if ls != rs:
					q.add(rs)

		i += m.pop(s)

	# print "final: "
	# print "t=", t, "n=", n, "ls=", ls, "rs=",rs,"q=", q,"m=", m,"i=", i 
	if len(q) == 0:
		rs, ls = 0, 0

	print "Case #%d: %d %d" % (t+1, max(ls,rs), min(ls,rs))
