
import sys

fin = open('B-large.in', 'r')
fout = open('B-large.out', 'w')	# sys.stdout #

def test_med(l, r, m):
	if l<m and m<r:
		v = 1 + max(solve(l,m), solve(m,r))
		
		m1 = m-1
		while m1>l:
			v1 = 1 + max(solve(l,m1), solve(m1,r))
			if v1 < v:
				#print "warn: m is not computed properly! (down)"
				return False
			elif v1 > v:
				break
			m1 -= 1
			
		m1 = m1+1
		while m1<r:
			v1 = 1 + max(solve(l,m1), solve(m1,r))
			if v1 < v:
				#print "warn: m is not computed properly! (up)"
				return False
			elif v1 > v:
				break
			m1 += 1

	else:
		#print "warn: m not in range"
		return False
		
	return True

def solve(l, r):
	if l*C >= r:
		return 0
	
	m = int((l*r) ** 0.5)
	#m_1 = m
	val1 = max(solve(l,m), solve(m,r)) if l<m and m<r else 1000000
	
	m = int((l*r) ** 0.5) + 1
	#m_2 = m
	val2 = max(solve(l,m), solve(m,r)) if l<m and m<r else 1000000

	#if not test_med(l, r, m_1) and not test_med(l, r, m_2):
	#	print "warn: general %d %d %d" % (l, r, m_1)
	
	val = 1 + min(val1, val2)
	return val

T = int(fin.readline())
for test in range(0, T):
	L, P, C = map(int, fin.readline().split())
	ans = solve(L, P)
	fout.write("Case #%d: %d\n" % (test+1, ans))

