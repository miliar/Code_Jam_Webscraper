
import math, itertools

s = []

def calc_time(n, c, f, x):
	global s
	if n == 0:
		s = [0]
	else:
		s.append(s[n - 1] + c/(2 + (n - 1)*f))
	return s[n] + x/(2 + n*f)

def solve(c, f, x):
	n_max = int(math.ceil((x - 2)/f))
	t_min = None
	for i in itertools.count(0):
	# for i in xrange(0, n_max + 1):
		ti = calc_time(i, c, f, x)
		# print '{0}: {1:0.07f}'.format(i, ti)
		if t_min == None:
			t_min = ti
		elif ti < t_min:
			t_min = ti
		else:
			break
	return t_min

t = input()
for i in xrange(t):
	[c, f, x] = [float(_) for _ in raw_input().split()]
	print 'Case #{0}: {1:0.07f}'.format(i + 1, solve(c, f, x))
