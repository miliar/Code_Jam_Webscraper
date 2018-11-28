#!/usr/bin/python

import sys

def ans(fp):
	ctr = 1
	line_no = int(fp.readline())
	while ctr <= 4:
		if ctr == line_no:
			line = fp.readline()
		else:
			fp.readline()
		ctr += 1

	return line.rstrip()

def case(fp):
	ans1 = ans(fp)
	ans2 = ans(fp)
	num1 = [int(n) for n in ans1.split()]
	num2 = [int(n) for n in ans2.split()]
	r = [i for i in num1 if i in num2]

	if(len(r) == 0):
		return 'Volunteer cheated!'
	elif(len(r) == 1):
		return str(r[0])
	elif(len(r) > 1):
		return 'Bad magician!'

if __name__ == "__main__":
	fp = open(sys.argv[1], 'r')
	test_cases = int(fp.readline())
	ctr = 1
	while ctr <= test_cases:
		res = case(fp)
		print('Case #%d: %s' % (ctr, res))
		ctr += 1
	fp.close()
