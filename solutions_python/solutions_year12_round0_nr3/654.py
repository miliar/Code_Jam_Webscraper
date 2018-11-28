import string
import math

def prepare_data(data):
	numbers = data.split()
	A = int(numbers[0])
	B = int(numbers[1])
	return (A, B)

def get_order(B):
	return int(math.log(B, 10))

def multiplier(B):
	return 10 ** get_order(B)

def get_next_number(number, mult):
	return (number % 10) * mult + int(number / 10)

def howMuchBiggerNumber(start_number, last_number):
	current_number = start_number
	count = 0
	mult = multiplier(last_number)
	found_elemnts = set()
	for x in xrange(get_order(start_number)):
		next_number = get_next_number(current_number, mult)
		if next_number > start_number and next_number <= last_number and next_number not in found_elemnts:
			count+=1
			found_elemnts.add(next_number)
		current_number = next_number
	return count

def solve(data):
	A, B = prepare_data(data)
	result = 0
	for x in xrange(A, B + 1):
		result += howMuchBiggerNumber(x, B)
	return result

if __name__ == '__main__':
	import sys
	T = int(sys.stdin.readline())
	for i in xrange(T):
		input_str = sys.stdin.readline().strip()
		res = solve(input_str)
		print "Case #%d: %s" % (i + 1, res)	
