import sys
rl=sys.stdin.readline

from decimal import *
getcontext().prec = 300

class memoize(dict):
	def __init__(self, func):
		self.func = func

	def __call__(self, *args):
		return self[args]

	def __clear__(self):
		self = {}

	def __missing__(self, key):
		result = self[key] = self.func(*key)
#		print key, " => ", result
		return result


a = ''
n = 0

def compute_violated(violated, relaxed_violated, digit, aj):
	if relaxed_violated:
		return (False, True)
	if violated:
		if digit < aj:
			return (False, True)
		else:
			return (True, False)
	return (digit > aj, False)

@memoize
def dp(idx, jdx, started, sum_square, relaxed, violated, relaxed_violated):

	if idx > jdx:
		if relaxed or (not relaxed and not violated):
			return 1
		return 0

	ret = 0
	# for i
	range_start = 1 if (started == idx) else 0
	range_end = 3 if relaxed else min(3, a[idx])

	for digit in xrange(range_start, range_end+1):
		next_sum_square = sum_square + digit * digit * (idx == jdx and 1 or 2)

		if next_sum_square < 10:

			ret += dp(idx + 1, jdx - 1, started, 
						next_sum_square,
						relaxed or (digit < a[idx]),
						*compute_violated(violated, relaxed_violated, digit, a[jdx])
						)
	return ret


def f(value):
	global a, n
	a = map(int, str(value))
	n = len(a)

	dp.clear()
	ret = 0
	for start in xrange(0, n):
#		print value, "start = ", start, ":", dp(start,n-1,start, 0, start>0, False, False)
		ret += dp(start, n - 1, start, 0, start > 0, False, False)

#	sys.stderr.write( str( (value, ret) ) + "\n" )
	return ret

def go(A, B):
	sA = Decimal(A).sqrt()
	sB = Decimal(B).sqrt()
	if sA == int(sA):
		sA = int(sA)
	else:
		sA = int(sA) + 1
	sB = int(sB)

	return f(sB) - f(sA - 1)



def debug():
	prev = None
	for i in xrange(2000):
		now = f(i)
		if prev != now:
			print i, now
			prev = now
	#return
		
	for i in [1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111 ]:
		print i, f(i)


def main():
	T=int(rl())
	for i in xrange(1,T+1):
		sys.stderr.write("%d / %d\n"% (i, T))

		A, B = map(int, rl().split())
		print "Case #%d: %d" % (i, go(A, B))

if __name__ == '__main__':
	main()
