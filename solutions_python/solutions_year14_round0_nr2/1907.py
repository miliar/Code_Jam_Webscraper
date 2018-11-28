
def solve(C,F,X):
	times = [float('inf')]
	time = 0.0
	R = 2.0
	while True:
		times.append(X/R+time)
		time += C/R
		R += F
		if times[-1]>=times[-2]:
			break
	return min(times)

def solve2(C,F,X):
	def time(R):
		return min(
			X/R,
			C/R + time(R+F)
		)
	return time(C,F,X)

T = int(raw_input())
for t in xrange(1,T+1):
	C,F,X = map(float, raw_input().split())
	print "Case #%d: %.7f" % (t, solve(C,F,X))
