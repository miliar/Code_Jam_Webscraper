import sys

def one_test():
	s, k = input().split()
	k = int(k)
	#print(s, k)
	s = list(s)
	ret = 0

	flip = lambda c: '+' if c == '-' else '-'

	for i in range(len(s) - k + 1):
		if s[i] == '-':
			ret += 1
			for j in range(i, i + k):
				s[j] = flip(s[j])

	if s.count('-') != 0:
		print("IMPOSSIBLE")
	else:
		print(ret)

def work(one_test):
	t = int(input())
	for i in range(1, t + 1):
		print("test {} started".format(i), file = sys.stderr)
		print("Case #{}: ".format(i), end = '')
		one_test()

work(one_test)