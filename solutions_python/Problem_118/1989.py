import math

def isPalindrome(suspect):
	length = len(suspect)
	if length <= 1:
		return True
	if suspect[0] != suspect[length - 1]:
		return False
	return isPalindrome(suspect[1:length-1])

def checker(begin, end, i):
	ctr = 0
	begin_sqrt = int( math.ceil(math.sqrt(begin)) )
	end_sqrt = int( math.floor(math.sqrt(end)) )
	for i in range(begin_sqrt, end_sqrt+1, 1):
		if isPalindrome( str(i) ):
			if isPalindrome( str( int( math.pow(i, 2) ) ) ):
				ctr += 1
	return ctr

	

input_file = open('small_input', 'r')
output_file = open('small_output', 'w')
#input_file = open('large_input', 'r')
#output_file = open('large_output', 'w')
num_intervals = int(input_file.readline())
output = ''

for i in range(1, num_intervals+1):
	intervals = input_file.readline().split()
	begin, end = int(intervals[0]), int(intervals[1])
	print begin, end
	output += 'Case #{0}: {1}\n'.format(i, checker(begin, end, i))
output_file.write(output)

output_file.close()
input_file.close()