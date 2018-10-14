import sys
import numpy as np
import itertools

def print_failure(i):
	print("Case #%d: IMPOSSIBLE"%i)

def print_ans(i, s):
	print("Case #%d: %d"%(i, s))

def convert_number(number):
	nr = []
	for dig in number:
		if dig == '+':
			nr.append(1)
		else:
			nr.append(-1)
	return np.array(nr)

def process_number(number, k, t, index):
	k = int(k)
	number = convert_number(number)
	summ = len(number)
	if sum(number) == summ:
		print_ans(index, 0)
		return
	it = 1
	limit = 1000
	
	for a in range(limit):
		i = next((i for i, x in enumerate(number) if x==-1), 0)
		if i > summ-k:
			i = summ-k
		middle = np.multiply(number[i:i+k], -1)
		# print(i, number, middle)
		number[i:i+k]=middle
		if sum(number) == summ:
			print_ans(index, it)
			return
		it += 1
	if it == limit+1:
		print_failure(index)

for i, line in enumerate(sys.stdin):
    if i == 0:
    	t = int(line)
    else:
    	data, k = line.split()
    	answer = process_number(data, k, t, i)
    	
