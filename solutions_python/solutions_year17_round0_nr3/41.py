import sys

def work(one_test):
	t = int(input())
	for i in range(1, t + 1):
		print("test {} started".format(i), file = sys.stderr)
		print("Case #{}: ".format(i), end = '')
		one_test()

def solve(n, k):
	count = {}
	count[n] = 1
	while True:
		now_max = max(count.keys())
		count_max = count.pop(now_max)
		#print(now_max, count_max, k)
		big = now_max // 2
		small = (now_max - 1) // 2
		if k <= count_max:
			return ' '.join((str(big), str(small)))
		k -= count_max
		count[big] = count.get(big, 0) + count_max
		count[small] = count.get(small, 0) + count_max
	raise AssertionError

def one_test():
	n, k = map(int, input().split())
	print(solve(n, k))

work(one_test)