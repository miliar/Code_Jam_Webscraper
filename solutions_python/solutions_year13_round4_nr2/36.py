def solve():
	n, p = map(int, raw_input().split())
	print foo(p, n), bar(p, n)
	
def bl(y, n):
	if n == 0:
		return 0
	if y == 0:
		return bl(y, n-1)
	else:
		return (1 << (n-1)) + bl((y-1)/2, n-1)

def foo(p, n):
	low, high = 0, 2**n
	while (high - low) > 1:
		mid = (low + high) / 2
		if bl(mid, n) < p:
			low = mid
		else:
			high = mid
	return low

def bar(p, n):
	z = 2**n - 1
	low, high = 0, 2**n
	while (high - low) > 1:
		mid = (low + high) / 2
		if 2**n - bl(z - mid, n) <= p:
			low = mid
		else:
			high = mid
	return low

if __name__ == '__main__':
	t = int(raw_input())
	for t in xrange(1, t+1):
		print 'Case #%d:' % t,
		solve()

