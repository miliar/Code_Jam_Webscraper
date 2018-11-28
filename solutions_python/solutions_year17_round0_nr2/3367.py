import sys
input = sys.stdin.readlines()

def find_tidy(num_str):
	num_str = list(num_str)
	
	num = map(int, num_str)
	# print num
	mark = 0
	for i in range(len(num)-2, -1, -1):
		# print i
		if num[i] > num[i+1]:
			mark = i
			num[i] = num[i] - 1
			num[i+1:] = [9 for x in num[i+1:]]
	# print num
	num_str = map(str, num)
	# print num_str
	return int(''.join(num_str))


# find_tidy('54321')
# find_tidy('12534')
# find_tidy('11111111111901111110')

for i in range(1,len(input),1):
	elem = input[i]
	num_str = elem.rstrip('\n')
	val = find_tidy(num_str)
	output = "Case #" + str(i) + ":"
	print output,val