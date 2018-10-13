
def find_tidy(N):
	digits = [int(i) for i in str(N)]
	digits.reverse()

	for i in xrange(len(digits) - 1):
		if digits[i] < digits[i + 1]:
			for j in xrange(i + 1):
				digits[j] = 9
			digits[i + 1] -= 1

	digits.reverse()
	return int(''.join(map(str, digits)))

T = int(raw_input())

for i in xrange(T):
	N = int(raw_input())
	tidy = find_tidy(N)

	print "Case #%d: %d" % (i + 1, tidy)
