import math

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	stalls, people = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
	
	#people -= 1
	
	most_power = 1
	
	while most_power * 2 <= people:
		most_power *= 2
	
	remaining_people = people - (most_power -1)

	remaining_stalls = stalls - (most_power -1)
	
	stall_block = int(remaining_stalls / most_power)

	remaining_blocks = remaining_stalls % most_power
	
	if remaining_people > remaining_blocks:
		stall_block -= 1

	left = math.floor((float(stall_block) / 2.0))

	right = math.ceil((float(stall_block) / 2.0))
	
   
	print("Case #{}: {} {}".format(i, max(left, right),  min(left, right)))
	# check out .format's specification for more formatting options