import sys
from datetime import datetime
import itertools
import copy
from collections import deque
import bisect

def main(argv):
	start_time = datetime.now()
	filename = argv[1]
	output = argv[2]
	with open(filename) as infile:
		num_tests = int(infile.readline())
		with open(output, 'w+') as out:
			for test_num in range(num_tests):
				out.write('Case #{}: '.format(test_num + 1))
				n = int(infile.readline())
				n_blocks = map(float, infile.readline().split())
				k_blocks = map(float, infile.readline().split())
				k_blocks.sort()
				n_blocks.sort()
				#Deceitful War Scores
				n_points = 0
				k_copy = deque(k_blocks)
				for block in n_blocks:
					if block > k_copy[0]:
						n_points += 1
						k_copy.popleft()
					else:
						k_copy.pop()
				out.write('{} '.format(n_points))
				#War Scores
				n_points = 0
				k_copy = deque(k_blocks)
				for block in n_blocks:
					k_larger_blocks = [k_block for k_block in k_copy if k_block > block]
					k_choice = min(k_larger_blocks) if len(k_larger_blocks) > 0 else min(k_copy)
					if k_choice < block:
						n_points += 1
					k_copy.remove(k_choice)
				out.write('{}\n'.format(n_points))
	print 'Time taken: {}'.format(datetime.now() - start_time)

main(sys.argv)