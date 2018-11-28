import re

L, D, N = map(int, raw_input().split())

words = []
for i in range(D):
	words.append(raw_input())

for i in range(1, N + 1):
	pattern = raw_input()
	pattern = pattern.replace('(', '[').replace(')', ']')
	reg_exp = re.compile(pattern)
	count = 0
	for word in words:
		if reg_exp.match(word):
			count += 1
	print "Case #%d: %d" % (i, count)
