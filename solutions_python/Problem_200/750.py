from functools import wraps

memos = {}

def memoize(func):
	@wraps(func)
	def memoized(*args):
		if args not in memos:
			memos[args] = func(*args)
		return memos[args]
	return memoized


def solve(remainder, last_digit):
	if not remainder:
		return 0
	result = 0
	result = max(result, solve(remainder // 10, min(remainder % 10, last_digit)) * 10 + min(remainder % 10, last_digit))
	if remainder // 10:
		result = max(result, solve(remainder // 10 - 1, 9) * 10 + 9)
	return result

t = int(raw_input())
for case in xrange(t):
	n = int(raw_input())
	print 'Case #%d: %d' % (case + 1, solve(n, 10))
