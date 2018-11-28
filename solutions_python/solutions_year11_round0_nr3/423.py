
def solve(data):
	N, C = data
	if reduce(lambda a, b: a ^ b, C):
		return 'NO'
	return sum(C) - sorted(C)[0]

def get_input():
	N = int(raw_input())
	C = map(int, raw_input().split())
	return N, C

def main():
	T = int(raw_input())
	for i in xrange(T):
		print 'Case #%s: %s' % (i + 1, solve(get_input()))

if __name__ == '__main__':
	main()
