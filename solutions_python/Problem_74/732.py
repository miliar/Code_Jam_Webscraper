#!/usr/bin/python

num_test = int(raw_input())

for T in range(num_test):
	line = raw_input()
	nums = line.split(" ")
	N = int(nums[0])
	del nums[0]
	robots = [nums[i] for i in range(len(nums)) if i % 2 == 0]
	meters = [int(nums[i]) for i in range(len(nums)) if i % 2 == 1]
	o_pos,b_pos = 1,1
	o_pre,b_pre = 0,0
	now = 0
	
	for r,m in zip(robots,meters):
		if r == "O":
			dist = abs(m-o_pos) - (now-o_pre)
			
			if dist <=  0:
				now += 1
			else:
				now += dist + 1
			o_pre = now
			o_pos = m
		else:
			dist = abs(m-b_pos) - (now-b_pre)
			
			if dist <=  0:
				now += 1
			else:
				now += dist + 1
			b_pre = now
			b_pos = m
	print "Case #%d: %d" % (T+1,now)

			  
