import sys

# Find the last increasing digit, convert everything else to 9's
# 132 => 129
# 1000 => 999
# 7 => 7
# 111111111111111110 => 99999999999999999

def num_to_arr(num):
	arr = []
	while num > 0:
		arr.insert(0, num % 10)
		num //= 10
	return arr

def arr_to_num(arr):
	num = 0
	for i in xrange(len(arr)):
		num = num + arr[i] * 10 ** (len(arr) - i - 1)
	return num

def find_furthest_left(arr):
	for i in xrange(1, len(arr)):
		if arr[i] <= arr[i - 1]:
			return arr[i - 1], i - 1
	return arr[0], 0

def convert_past(arr, right_pos):
	for i in xrange(right_pos + 1, len(arr), 1):
		arr[i] = 9
	return arr

def decr_right(arr, right_pos):
	arr[right_pos] -= 1
	return arr

def all_incr(num):
	nums = num_to_arr(num)
	prev = nums[0]
	for n in nums:
		if n < prev:
			return False
		prev = n
	return True

def process(num):
	if all_incr(num):
		return num
	arr = num_to_arr(num)
	digit, pos = find_furthest_left(arr)
	arr = convert_past(arr, pos)
	arr = decr_right(arr, pos)
	result = arr_to_num(arr)
	return result

'''
1) Find the left end in an increasing sequence
2) Convert everything past that digit into 9s
3) Subtract this right digit by 1
'''





lines = [line.rstrip() for line in sys.stdin]
num_cases = int(lines[0])

for i, line in enumerate(lines[1:]):
	print "Case #{0}: {1}".format(i + 1, process(int(line)))
