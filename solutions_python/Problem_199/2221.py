from __future__ import print_function

t = int(raw_input())
for tn in range(t):
	s, k = raw_input().split()
	k = int(k)
	s = list(s)
	count = 0
	flag = 1
	for i in range(len(s)):
		if s[i] == '-':
			if i <= len(s) - k:
				count += 1
				for j in range(k):
					s[i + j] = '+' if s[i + j] == '-' else '-'
				# print(i, *s)
			else:
				print("Case #%d: IMPOSSIBLE" % (tn + 1))
				flag = 0
				break
	if flag == 1:
		print("Case #%d: %d" % (tn + 1, count))