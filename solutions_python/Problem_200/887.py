#!/bin/python
import sys

def toNum(num_list):
	
	value = 0
	exp = 1
	for i in num_list:
		value += i * exp
		exp *= 10
	return value

def splitNumber(v):
	number_list = []
	while (v):
		number_list.append(v % 10)
		v /= 10
	return (number_list)

n = int(raw_input().strip())
for cnt in range(n):
	v = raw_input().strip()
	v = int(v)
	num_list = splitNumber(v)
	# print(isTidy(num_list))
	start = 0
	for i in range(len(num_list) - 1):
		if (num_list[i] < num_list[i + 1]):
			for j in range(i + 1):
				num_list[j] = 9
			num_list[i + 1] -= 1

	cur_val = toNum(num_list)
	print ("Case #{}: {}".format(cnt + 1, cur_val))
