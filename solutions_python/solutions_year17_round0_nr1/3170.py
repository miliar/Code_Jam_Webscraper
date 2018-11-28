import sys
import re

file = open(sys.argv[1])
T = None
Case = 1

def flip(S, begin, end):
	S = list(S)
	for i in range(begin, end):
		if S[i] == '+':
			S[i] = '-'
		else:
			S[i] = '+'
	return ''.join(S)

for row in file:
	if T is None:
		T = int(row)
		continue
	S = row.split(' ')[0]
	K = int(row.split(' ')[1])
	Count = 0

	if S.find('-') == -1:
		Count = 0
	elif len(S) == K and S.find('+') != -1:
		Count = -1
	elif len(S) == K and S.find('+') == -1:
		Count = 1
	else:
		num = len(re.findall('-' * K, S))
		S = S.replace('-' * K, '+' * K, num)
		Count = Count + num
		while 1:
			num = S.find('-')
			if num == -1:
				break
			if num + K > len(S):
				Count = -1
				break
			S = flip(S, num, num + K)
			Count = Count + 1

	if Count >= 0:
		print("Case #%d: %d" % (Case, Count))
	else:
		print("Case #%d: IMPOSSIBLE" % Case)
	Case = Case + 1
	T = T - 1
	if T == 0:
		break
