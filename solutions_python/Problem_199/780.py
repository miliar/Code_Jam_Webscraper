import sys


T = int(raw_input())

for i in xrange(1, T + 1):
	cur_line = raw_input().split(" ")
	K = int(cur_line[1])
	
	S = list(cur_line[0])

	count = 0

	for j in xrange(0, len(S) - K + 1):
		if(S[j] == '-'):
			count += 1
			for k in xrange(j, j + K):
				if(S[k] == '+'):
					S[k] = '-'
				else:
					S[k] = '+'

	checker = True

	for j in xrange(len(S) - K, len(S)):
		if(S[j] == '-'):
			checker = False
			break

	result = "Case #" + str(i) + ": "

	if(checker):
		result += str(count)
	else:
		result += "IMPOSSIBLE"

	print result