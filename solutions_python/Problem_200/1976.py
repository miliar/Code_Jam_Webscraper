import os
import sys
current = os.getcwd()
outer = os.path.dirname(os.getcwd())
sys.path.append(current)
sys.path.append(outer)

from utils.io import *

flipping = {'-':'+', '+':'-'}

def main():
	start = time_in_ms()
	info = parse_data()
	raw_tests = info[0]
	output_file = info[1]
	results = []

	for idx, r_test in enumerate(raw_tests):
		print("Trying #"+str(idx))
		test = r_test
		results.append(solve(test))
		print(results[-1])

	##print(results)
	data_output(results, output_file)
	print("Time taken:",str(time_in_ms() - start)+"ms")

def solve(test):
	N=int(test[0])
	digits = [int(d) for d in str(N)]
	print(digits)

#	if is_tidy(digits):
#		return str(int("".join(map(str,digits))))

	previous_tidy(digits)
	print(digits)
	return str(int("".join(map(str,digits))))


def is_tidy(digits):
	c = 0
	for d in digits:
		if c>d:
			return False
		else:
			c=d
	return True

def previous_tidy(digits):
	replace = True

	while replace:
		replace = False

		for idx,d in enumerate(digits[1:]):
			#print(digits,replace,idx)
			if replace:
				digits[1+idx] = 9

			elif digits[idx]>digits[1+idx]:
				digits[idx] -= 1
				digits[1+idx] = 9
				replace = True

if __name__ == '__main__':
	main()


