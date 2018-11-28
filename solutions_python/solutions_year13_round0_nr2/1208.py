#/usr/bin/python

def check_row(row, x):
	return max([0] + row[:x]) > row[x] or max(row[x + 1:] + [0]) > row[x]

def analyze_lawn(lawn, case_num, n, m):
	for x in xrange(n):
		for y in xrange(m):
			if check_row(lawn[x], y) and check_row([lawn[i][y] for i in xrange(n)], x):
				print "Case #%(num)d: NO" % {"num": case_num + 1}
				print x, y
				return

	print "Case #%(num)d: YES" % {"num": case_num + 1}

def main():
	num_cases = int(raw_input())

	for i in xrange(num_cases):
		n, m = (int(x) for x in raw_input().split())

		lawn = [0] * n
		for l in xrange(n):
			lawn[l] = [int(x) for x in raw_input().split()]

		analyze_lawn(lawn, i, n, m)

if __name__ == '__main__':
	main()