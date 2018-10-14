# Read all the intervals and sort according to bottom limit
# for every square
# if a number is past a certain upper limit, pop the entry from both the initial array and the active stack and print the result
# if a number is past a certain lower limit put it in a stack which stores the currently active intervals
# if a we reach a fair square palindrome, add 1 to all the active intervals



# checking if palindrome:

# convert value to string
# 

import sys



output = []
def mark(test_case, val):
	global output
	output.append((test_case, 'Case #'+str(test_case+1)+': '+str(val)))
def p():
	global output
	output = sorted(output, key=lambda casenum: casenum[0])
	for i in output:
		print i[1]


def is_palindrome(val):
	val = str(val)
	for i in range(len(val)/2):
		if not val[i] == val[-i-1]:
			return False
	return True


fname = sys.argv[1]
stream = open(fname)

input_data = stream.read()

input_data = input_data.split('\n')
	

test_cases = int(input_data.pop(0))
ranges = []
i = 0
while i < test_cases:
	temp = input_data.pop(0)
	temp = temp.split(' ')
	temp[0] = long(temp[0])
	temp[1] = long(temp[1])
	temp = (temp[0], temp[1], i)
	ranges.append(temp)
	i = i+1

ranges = sorted(ranges, key=lambda lowerlimit: lowerlimit[0])	

max_limit =  max(ranges, key=lambda upperlimit: upperlimit[1])[1]

min_limit = ranges[0][0]

i = min_limit//2
max_limit = max_limit//2

active_intervals = []
while i <= max_limit:
	square = i*i
	while len(ranges)>0 and square >= ranges[0][0]:
		active_intervals.append([ranges.pop(0), 0])
	j = 0
	while j < len(active_intervals):
		if square > active_intervals[j][0][1]:
			temp = active_intervals.pop(j)
			mark(temp[0][2], temp[1])
		else:
			j = j+1
	if is_palindrome(i) and is_palindrome(square):
		for interval in active_intervals:
			interval[1] = interval[1] + 1
	i = i+1


p()
