import sys

def work(one_test):
	t = int(input())
	for i in range(1, t + 1):
		print("test {} started".format(i), file = sys.stderr)
		print("Case #{}: ".format(i), end = '')
		one_test()

def make_tidy(s, fix):
	s = s[:]
	for i in range(fix - 1):
		if s[i] > s[i + 1]:
			return None
	for j in range(fix, len(s)):
		s[j] = '9'
	return ''.join(s)

def solve(s):
	ans = make_tidy(s, len(s))
	if ans:
		return ans
	for pos in range(len(s) - 1, -1, -1):
		here = ord(s[pos]) - ord('0')
		lowest = 1 if pos == 0 else 0
		for now in range(here - 1, lowest - 1, -1):
			s[pos] = chr(ord('0') + now)
			ans = make_tidy(s, pos + 1)
			if ans:
				return ans
	return ''.join(['9'] * (len(s) - 1))

def one_test():
	s = list(input())
	print(solve(s))

work(one_test)
# for i in range(456, 567):
# 	print(i, solve(list(str(i))))