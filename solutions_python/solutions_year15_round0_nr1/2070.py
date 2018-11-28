T = int(raw_input())


def solve(digits):
	people_standing = 0
	people_added = 0
	for i in range(len(digits)):
		if digits[i] == 0:
			continue
		if people_standing >= i:
			people_standing += digits[i]
		else:
			people_added += (i - people_standing)
			people_standing += (i - people_standing) + digits[i]
	return people_added


for i in xrange(T):
	_, digits = list(raw_input().split(' '))
	digits = map(int, list(digits))
	print 'Case #{0}: {1}'.format(i + 1, solve(digits))