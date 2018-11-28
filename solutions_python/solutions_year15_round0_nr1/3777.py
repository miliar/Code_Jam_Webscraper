#!/usr/bin/env python

def num_friends_recursive(level, dist):
	if level == 0:
		return 0
	result = num_friends_recursive(level-1, dist)	
	if (dist[level-1] + result) >= level:
		return result
	return 1 + result

def cumsum(list_to_cum):
	cum_list = []
	s = 0
	for num in list_to_cum:
		s += num
		cum_list.append(s)
	return cum_list



def standing_ovation(input_file):
	fh = open(input_file, 'r')
	result = open('result.out', 'w')
	num_cases = int(fh.readline())
	for case in range(1, num_cases+1):
		level_str, distribution_str = fh.readline().split()
		level = int(level_str)
		distribution = []
		for num in list(distribution_str):
			distribution.append(int(num))
		print level
		print distribution
		dist_cum = cumsum(distribution)

		bring_friends_num = num_friends_recursive(level, dist_cum)
		wr_str = 'Case #' + str(case) + ': ' + str(bring_friends_num) + '\n'
		result.write(wr_str)
	fh.close()
	result.close()





standing_ovation('/Users/ammeurer/GoogleCodeJam/A-small-attempt1.in.txt')
