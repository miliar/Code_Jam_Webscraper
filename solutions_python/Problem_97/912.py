#!/usr/bin/env python
# -*- coding: utf-8 -*-

FILE_NAME = 'C-small-attempt0'
IN_FILE = FILE_NAME + '.in'
OUT_FILE = FILE_NAME + '.out'

f = open(IN_FILE, 'r')
src = f.read().split('\n')
f.close()

case_num = int(src.pop(0))
case_count = 0
result = ''

def recycle (num):
	result = set()
	line = str(num)
	for i in range(1, len(line)):
		new = int(line[i:] + line[:i])
		if new != num:
			result.add(new)
	return result

print recycle(12)


print('############ start #################')
for case_count in range(case_num):
	s = src.pop(0).strip().split(' ')
	a, b = [int(score) for score in s]
	nums = set(range(a, b))

	count = 0
	print "start: %d - %d" % (a, b)
	while len(nums):
		n = nums.pop()
		rec = recycle(n)
		rec = set(filter(lambda x: a <= x and x <= b, rec))
		if len(rec):
			print "found: %d => %s" % (n, rec)
			count += (len(rec) + 1) * len(rec) / 2
			nums -= rec

	ans = 'Case #%d: %d\n' % (case_count + 1, count)
	print ans
	result += ans
print('############ end ###################')



f = open(OUT_FILE, 'w')
f.write(result)
f.close()