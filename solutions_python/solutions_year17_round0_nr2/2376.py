from __future__ import print_function

t = int(raw_input())
for tn in range(t):
	num = list(raw_input())
	for i in range(len(num)):
		flag = 0
		for j in range(1, len(num) - i):
			if num[j - 1] > num[j]:
				num[j - 1] = chr(ord(num[j - 1]) - 1)
				num = num[:j] + ['9' for _ in range(len(num) - j)]
				flag = 1
		if flag == 0:
			break
	i = 0
	while num[i] == '0':
		i += 1
	print("Case #%d: %s" % (tn + 1, ''.join(num[i:])))