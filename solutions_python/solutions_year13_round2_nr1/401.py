#! /usr/bin/python3

counter = 1
def print_case(operation_count):
	global counter
	print("Case #{}: {}".format(counter, str(operation_count)))
	counter = counter + 1

def resolve_motes(size_start, array):
	
	#special case :
	if size_start == 1 :
		return len(array)

	if (len(array) == 0):
		return 0
	if (array[0] < size_start):
		size_start = size_start + array[0]
		del array[0]
		return resolve_motes(size_start, array)
	if (array[0] >= size_start):
		size_start = size_start + size_start - 1
		return min(len(array), 1 + resolve_motes(size_start, array))

total_numbers = int(input())
for i in range(total_numbers):
#1st is start, 2nd is number of motes
	cas = input().split()
	size_start = int(cas[0])
	motes = input().split()
	motes = [int(number) for number in motes]
	motes.sort()

	print_case(resolve_motes(size_start, motes))

