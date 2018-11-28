import sys
import numpy as np
import itertools

def print_failure(i):
	print("Case #%d: IMPOSSIBLE"%i)

def print_ans(i, s):
	print("Case #%d: %d"%(i, s))

def find_ans(last_number, ind):
	if last_number < 10:
		print_ans(ind, last_number)
		return
	tidy = 0

	digits = [int(x) for x in str(last_number)]
	diff = np.diff(digits)[::-1]
	i = len(diff)-next((i for i, x in enumerate(diff) if x==-1), 0)-1
	number = int(''.join(map(str,digits)))

	if min(np.diff(digits)) >= 0:
			print_ans(ind, number)
			return

	for s in range(10000):
		if digits[i] == 0:
			i -= 1
		else:
			digits[i]-=1
			if i < len(digits):
				for index in range(i+1, len(digits)):
					digits[index]=9
		diff = np.diff(digits)[::-1]
		number = int(''.join(map(str,digits)))

		# exit()
		if min(np.diff(digits)) >= 0:
			print_ans(ind, number)
			return


for i, line in enumerate(sys.stdin):
    if i == 0:
    	t = int(line)
    else:
    	last_number = int(line)
    	find_ans(last_number, i)
