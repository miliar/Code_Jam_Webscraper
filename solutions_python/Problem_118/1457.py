from math import sqrt, ceil
from sys import *

def is_pal(num):
	array = []
	tmp = num
	while tmp > 0:
		array.append(tmp % 10)
		tmp = tmp // 10
	for i in range(int(len(array) / 2)):
		if array[i] != array[-i -1]:
			return False
	return True

T = int(stdin.readline())
for t in range(T):
	line = stdin.readline().split(' ')
	begin, end = int(line[0]), int(line[1])

	ok = 0
	begin_sqrt = ceil(sqrt(begin))
	end_sqrt = int(sqrt(end))
	for cur_sqrt in range(begin_sqrt, end_sqrt + 1):
		if is_pal(cur_sqrt) and is_pal(cur_sqrt * cur_sqrt):
			ok += 1
	print('Case #', t + 1, ': ', ok, sep='')