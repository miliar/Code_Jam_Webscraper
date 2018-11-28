#!/usr/bin/env python3

# flipper flips k consec pancakes
input = open('A-large.in')
out = open('A-large-output.txt', 'w')
lines = input.readlines()
num_cases = lines[0]
cases = lines[1:]

def flip(s, k, flips):
	while True:
		#print s + '  ' + str(k) + '  ' + str(flips)
        	if '-' not in s:
			return flips

		if len(s) < k:
			return 'IMPOSSIBLE'

		if s[0] != '-':
			s = s[1:]
        		#return flip(s[1:], k, flips)
			continue

		for i in range(k):
			s = s[0:i] + ('-' if s[i] == '+' else '+') + s[i+1:]
		flips += 1

for i, case in enumerate(cases):
	if i >= num_cases:
		print 'I HAVE MORE CASES THAN EXPECTED'

	[s, k] = case.split(' ')
	flips = flip(s, int(k), 0)
	case_output = 'Case #'+ str(i+1) + ': ' + str(flips)
	print(case_output)
	out.write(case_output + '\n')

out.close()
