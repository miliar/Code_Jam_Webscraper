#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import *

FILE_NAME = 'A-small-attempt2'
IN_FILE = FILE_NAME + '.in'
OUT_FILE = FILE_NAME + '.out'

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

case_num = int(src.pop(0))
case_count = 0
result = ''

def option1(current, total, probs):
	c_prob = reduce(lambda x, y: x * y, probs)
	expect = c_prob * (total - current + 1) + (1 - c_prob) * (total * 2 - current + 2)
	return expect

def option2(current, total, probs):
	expect = total * 2
	for i in range(1, current):
		c_prob =  reduce(lambda x, y: x * y, probs[:-1])
		c_ex = i * 2 + total - current + 1
		e = c_prob * c_ex + (1-c_prob) * (c_ex + total + 1)
		expect = min(expect, e)
	e = current + total + 1
	return min(expect, e)

def option3(current, total, probs):
	expect = total + 2
	return expect

print('############ start #################')
for case_count in range(case_num):
	current, total = [int(char) for char in src.pop(0).strip().split(' ')]
	probs = [Decimal(char) for char in src.pop(0).strip().split(' ')]
	ans = min([option1(current, total, probs), option2(current, total, probs), option3(current, total, probs)])
	print current, total, probs
	print([option1(current, total, probs), option2(current, total, probs), option3(current, total, probs)])
	ans = 'Case #%d: %06f\n' % (case_count + 1, ans)
	print ans
	result += ans
print('############ end ###################')


f = open(OUT_FILE, 'w')
f.write(result)
f.close()