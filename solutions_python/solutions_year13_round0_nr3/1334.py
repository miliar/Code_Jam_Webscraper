import sys, math
class Finish: pass
p = sys.stdout.write
T = int(raw_input())
def isp(x):
	s = str(x)
	l = len(s)
	for i in xrange(l / 2):
		if s[i] != s[l - 1 - i]: 
			return False
	return True

for c in xrange(T):
	p('Case #%d: ' % (c + 1))
	A, B = map(int, raw_input().split())
	a, b = map(int, map(math.ceil, map(math.sqrt, (A, B))))
	t = 0
	for x in xrange(a, b + 1):
		p2 = int(math.pow(x, 2))
		if p2 > B:
			break
		if isp(x) and isp(p2):
			t += 1
			#print x, 'yes'
		else:
			#print x, 'no'
			pass
	p(str(t))
	try:
		pass
	except Finish:
		pass
	p('\n')

