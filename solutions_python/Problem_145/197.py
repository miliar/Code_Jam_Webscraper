from fractions import gcd

def frac_sub(a):
	return a[1] - a[0], a[1]

pow_two = []

for i in range(0, 41):
	pow_two.append(2**i)

cases = int(raw_input())

for case_no in xrange(1, cases+1):
	a, b = map(int, raw_input().split("/"))

	g = gcd(a, b)
	a, b = a/g, b/g

	answer = 0

	while a < b:
		a = a * 2
		answer += 1

	if b not in pow_two:
		answer = -1

	if answer == -1:
		print "Case #%d: impossible" % case_no
	else:
		print "Case #%d: %d" % (case_no, answer)