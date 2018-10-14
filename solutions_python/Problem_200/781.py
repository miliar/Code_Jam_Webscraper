#!/bin/usr/env python

def is_tidy(s):
	size = len(s)
	for i in range(1, size):
		if s[i - 1] > s[i]:
			return (0)
	return (1)


def	make_tidy(s):
	size = len(s)
	prev = s[0]
	i = 1
	while i < size:
		if s[i - 1] > s[i]:
			break
		i += 1
	j = i - 1
	while j > 0:
		if int(s[j - 1]) <= int(s[j]) - 1:
			break
		j -= 1
	out = ''
	if j == 0 and s[0] == '1':
		ind = 1
	else:
		ind = 0
		while ind < j:
			out = out + s[ind]
			ind += 1
		out = out + str(int(s[ind]) - 1)
		ind += 1
	while ind < size:
		out = out + '9'
		ind += 1
	return (out)

t = int(raw_input())

for tn in range(t):
	n = raw_input()
	if is_tidy(n):
		output = n
	else:
		output = list(n)
		output = make_tidy(n)
#	print("Case #" + str(tn + 1) + ": " + str(output))
	print("Case #" + str(tn + 1) + ": " + str(output))
