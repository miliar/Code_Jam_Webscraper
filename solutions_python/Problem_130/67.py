def log_(x):
	y = x
	r = 0
	while x > 0:
		r = r + 1
		x = x >> 1
	return r - 1

def f(n, p):
	L = 0 
	R = (1 << n) - 1
	while L < R:
		mid = (L + R + 1) >> 1
		i = log_(mid + 1)
		T = (1 << n) - (1 << (n - i)) + 1
		if T <= p:
			L = mid
		else:
			R = mid - 1
	return L

def g(n, p):
	L = 0 
	R = (1 << n) - 1
	while L < R:
		mid = (L + R + 1) >> 1
		i = log_((1 << n) - mid)
		T = 1 << (n - i)
		if T <= p:
			L = mid
		else:
			R = mid - 1
	return L


if __name__ == "__main__":
	T = int(raw_input())
	cas = 1
	while T - cas >= 0:
		n, p = map(int, raw_input().split())
		print "Case #{0}: {1} {2}".format(cas, f(n, p), g(n, p))
		cas = cas + 1
