from math import ceil, floor

import math

t = int(input())
for case_number in range(1, t + 1):
	stalls_s, people_s = input().split(" ")
	stalls, people = int(stalls_s), int(people_s)
	
	#if case_number != 10:
	#	continue

	#print(stalls, people)
	
	people_going = 1
	level = 0

	people_left = people
	while(people_left > people_going):
		level += 1
		people_left -= people_going
		people_going *= 2

	#print(level, stalls, people_going, people_left, people_left / people_going)
	#print()
	size_float = stalls
	size_min = stalls
	size_max = stalls
	for a in range(level):
		size_float -= 1
		size_float /= 2
		size_min -= 1
		size_min = floor(size_min / 2)
		size_max -= 1
		size_max = ceil(size_max / 2)
		#print(a, size_min, size_max, size_float)

	segment = people_left / people_going
	portion = size_float - size_min
	#print()
	large = segment <= portion
	#print(segment,'<', portion, '->', large)

	r_size = size_max if large else size_min
	
	r_size -= 1
	r_min = floor(r_size / 2)
	r_max = ceil(r_size / 2)
	#print(r_size)
	
	print("Case #{}: {} {}".format(case_number, r_max, r_min))
	#break
