#!/usr/bin/env python3

# Find last non-decending number before n
input = open('B-large.in')
out = open('B-large-output.txt', 'w')
lines = input.readlines()
num_cases = lines[0]
cases = lines[1:]

for case_num, case in enumerate(cases):
	if case_num >= num_cases:
		print 'I HAVE MORE CASES THAN EXPECTED'

	n = int(case)
	#print(str(n))

	i = len(str(n)) - 1
	while i > 0:
		#print 'n: ' + str(n) + ' i: ' + str(i) + ' n-i:' + str(n)[-i] + ' n-i-1:' + str(n)[-i-1]
		if str(n)[-i] < str(n)[-i-1]:
			if str(n)[-i] == '0':
				n -= int(str(n)[-i:])+1
			else:
				n -= pow(10, i-1)
			i = len(str(n)) - 1
		else:
			i -= 1

	case_output = 'Case #'+ str(case_num+1) + ': ' + str(n)
	print(case_output)
	out.write(case_output + '\n')

out.close()
