# Andy Rock
# May 13, 2017
# 
# Round 2 2017: Problem A. 

from math import ceil

for T in xrange(1, int(raw_input()) + 1):

	N, P = map(int, raw_input().split())
	G = map(int, raw_input().split())

	freq = [0] * P
	for g in G:
		freq[g % P] += 1

	ans = freq[0]

	if P == 2:
		ans += (freq[1] + 1) / 2
	elif P == 3:
		if freq[1] == freq[2]:
			ans += freq[1]
		elif freq[1] > freq[2]:
			num = freq[1] - freq[2]
			ans += freq[2] + ceil(num / 3.)
		else:
			num = freq[2] - freq[1]
			ans += freq[1] + ceil(num / 3.)
	elif P == 4:
		ans += freq[2] / 2
		freq[2] %= 2
		if freq[1] == freq[3]:
			ans += freq[1]
			ans += freq[2]
		elif freq[1] > freq[3]:
			num = freq[1] - freq[3]
			ans += freq[3]
			ans += num / 4
			num %= 4
			if freq[2] == 0:
				ans += num != 0
			else:
				ans += freq[2] + (num == 3)
		else:
			num = freq[3] - freq[1]
			ans += freq[1]
			ans += num / 4
			num %= 4
			if freq[2] == 0:
				ans += num != 0
			else:
				ans += freq[2] + (num == 3)

	print 'Case #%d: %d' % (T, ans)
