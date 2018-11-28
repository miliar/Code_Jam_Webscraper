def solve(case_number):
	sn = raw_input()
	n = [int(k) for k in sn]
	change_to_smaller = 0
	for i in range(len(n) - 1):
		if n[i] > n[i + 1]:
			change_to_smaller = n[i]
			break

	if change_to_smaller:
		index = n.index(change_to_smaller)

		n[index] = int(change_to_smaller) - 1
		for i in range(index + 1, len(n)):
			n[i] = 9

	res = ''
	if n[0] > 0:
		res = str(n[0])

	for i in range(1, len(n)):
		res += str(n[i])

	print "Case #{}: {}".format(case_number, res)

t = int(raw_input())  # read a line with a single integer
for case in xrange(1, t + 1):
	solve(case)

'''
python solution.py <small.in> small.out
python solution.py <large.in> large.out
'''