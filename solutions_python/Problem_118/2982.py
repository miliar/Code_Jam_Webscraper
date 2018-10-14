#!/usr/bin/python3
from math import sqrt

for x in range(1, int(input())+1):
	y = 0
	A, B = input().split(' ')
	for i in range(int(A), int(B)+1):
		sqrt_i = sqrt(i)
		int_sqrt = int(sqrt_i)
		if sqrt_i == int_sqrt:
			str_i = str(int_sqrt)
			list_i = list(str_i)
			list_i.reverse()
			if str_i == ''.join(list_i):
				str_i = str(i)
				list_i = list(str_i)
				list_i.reverse()
				if str_i == ''.join(list_i):
					y += 1
	print('Case #%d: %d' % (x, y))

