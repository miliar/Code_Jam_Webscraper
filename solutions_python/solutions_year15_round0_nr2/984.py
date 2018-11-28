import math
import time

'''
for x in range(int(raw_input())):
	raw_input() # just need to go to next line
	num_list = map(int,raw_input().split(' '))
	done = False
	splits = 0
	while not done:
		max_num = max(num_list)
		max_num_half = (max_num / 2) + (max_num % 2)
		new_num_list = []
		pot_splits = 0
		for num in num_list:
			if num >= max_num_half:
				if num / 2 + (num % 2) + splits + pot_splits < num:
					pot_splits += 1
					new_num_list.append(max_num_half)
					new_num_list.append(num - max_num_half)
				else:
					done = True
					pot_splits = 0
					break
			else:
				new_num_list.append(num)
		splits += pot_splits
		print num_list
		print splits
		if not done:
			num_list = new_num_list
	print 'Case #%d: %d' % (x+1,splits + max(num_list))

'''
for t in range(int(raw_input())):
	raw_input() # just need to go to next line
	num_list = map(int,raw_input().split(' '))
	orig_len = len(num_list)
	num_list = [num_list]
	for x in num_list:
		for y in x:
			for index in range(0,y):
				if y - index > 0 and index > 0:
					if y / 2 + (y % 2) + len(x) - orig_len < y:
						num_list.append([index,y-index] + x[:x.index(y)] + x[x.index(y) + 1:])
		if all(x == 1 for x in num_list):
			break
		#print num_list

	lowest = 9999999999
	for nums in num_list:
		splits = len(nums) - orig_len
		max(nums) + splits
		if max(nums) + splits < lowest:
			lowest_num = nums
			lowest = max(nums) + splits
	print 'Case #%d: %d' % (t+1,lowest)
	#print lowest_num