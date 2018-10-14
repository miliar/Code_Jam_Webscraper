
def flip(s):

	return "".join(['+' if x == '-' else '-' for x in s])

test_case = int(input())

for tc in range(test_case):

	s, n = input().split(' ')
	l = len(s)
	ans = 0
	n = int(n)
	imp = False

	for i in range(len(s)):
		if s[i] == '-':
			if i + n > l:
				imp = True
			else:
				s = s[:i] + flip(s[i:i + n]) + s[i + n:]
				ans += 1

	if imp:
		print("Case #{}:".format(tc + 1), "IMPOSSIBLE")
	else:
		print("Case #{}:".format(tc + 1), ans)
				
