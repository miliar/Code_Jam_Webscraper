import math, time
import numpy as np
from pprint import pprint
from sortedcontainers import SortedDict
from multiprocessing import Pool

def divide(n):
	mid = math.ceil((n+1)/2.)
	return (mid -1, n - mid)

def get_left_right(data):
	#print ("N = %d, k = %d" % (N, k))
	N, k = data
	upper_bound = 2**(math.floor(math.log(N, 2))) - 1
	if N == k or (k > upper_bound):
		return (0, 0)

	left, right = divide(N)
	if k == 1:
		return left, right

	if left != right:
		sub_n = {left: [left], right: [right]}
	else:
		sub_n = {left: [left, left]}

	k_ = 2
	while(True):
		keys = sorted(sub_n.keys())
		#print (keys)
		max_n = keys[-1]
		#print ("max n=%d" % max_n)
		max_l, max_r = divide(max_n)
		#print (max_l, max_r)
		del sub_n[max_n][0]
		if len(sub_n[max_n]) == 0: del sub_n[max_n]

		#sub_n = np.delete(sub_n, max_i)
		if max_l in sub_n:
			sub_n[max_l].append(max_l)
		else:
			sub_n[max_l]= [max_l]

		if max_r in sub_n:
			sub_n[max_r].append(max_r)
		else:
			sub_n[max_r] = [max_r]

		#print ("k=%d, left=%d, right=%d" % (k_, left, right))
		#print ("new: ", sub_n)
		if k_ == k or (max_l <= 0 and max_r <= 0 ):
			#print (max_l, max_r)
			break

		k_ += 1

	return max(0,max_l), max(0,max_r)


start_time = time.time()
input_file_name = 'C-small-2-attempt1.in'
output_file_name = 'c.out'

output_line_template = "Case #%d: %d %d"
outputs = []

with open(input_file_name, 'r') as input_file:
	num_tests = int(input_file.readline().strip())
	test_data = []
	for test_id in range(1, num_tests+1):
		line = input_file.readline().strip()
		N, k = map(int, line.split())
		#left, right = get_left_right(N, k)
		test_data.append((N, k))

p = Pool(10)
outputs =  p.map(get_left_right, test_data)

outputdata = []
for i, output in enumerate(outputs):
	outputdata.append(output_line_template % (i+1, output[0], output[1]))

with open(output_file_name, 'w') as output_file:
	output_file.write('\n'.join(outputdata))

print ("Took %s seconds." % (time.time() - start_time))
	
'''outputs.append(output_line_template % (test_id, left, right))
if test_id % 10 == 0:
	print ("%d examples completed" % test_id)

with open(output_file_name, 'w') as output_file:
output_file.write('\n'.join(outputs))

print ("Took %s seconds." % (time.time() - start_time))'''

