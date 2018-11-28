#!/usr/bin/env python
#coding: utf-8
import sys

#1行目
test_n =  int(raw_input())
for c, line in enumerate(sys.stdin.read().splitlines()):
	add_n = 0
	stand_n = 0
	Smax = line.split(' ')[0]
	for sy_level, n in enumerate(line.split(' ')[1]):
		if stand_n >= sy_level:
			stand_n = stand_n + int(n)
		else:
			add_n = add_n + (sy_level - stand_n)
			stand_n = stand_n + (sy_level-stand_n) + int(n)
	#print "Case #%d: %d" % (line, add_n)
	print "Case #"+str(c+1)+":", add_n
