#!/usr/bin/env python
# encoding: utf-8

import sys, os, re

f = open('./input.txt')
o = open('./output.txt', 'w')
T = int(f.readline())

for case in range(1, T+1):
	first_answer = int(f.readline())
	first_square = [
		map(int, f.readline().split(' ')),
		map(int, f.readline().split(' ')),
		map(int, f.readline().split(' ')),
		map(int, f.readline().split(' '))
	]

	second_answer = int(f.readline())
	second_square = [
		map(int, f.readline().split(' ')),
		map(int, f.readline().split(' ')),
		map(int, f.readline().split(' ')),
		map(int, f.readline().split(' '))
	]

	first_numbers = first_square[first_answer-1]
	second_numbers = second_square[second_answer-1]

	numbers = set(first_numbers) & set(second_numbers)
	if len(numbers) == 1:
		o.write("Case #%s: %s\n" % (case, numbers.pop()))
	elif len(numbers) == 0:
		o.write("Case #%s: Volunteer cheated!\n" % case)
	else:
		o.write("Case #%s: Bad magician!\n" % case)

f.close()
o.close()
