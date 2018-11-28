#!/usr/bin/env python
""" 
    text_messaging.py
    solution to Text Messaging problem
    
    Copyright (C) 2008 Masood Behabadi <masoodbeh@gmail.com>
"""
from sys import stdin

cases = []  # list of cases

# parsing input data
totalCases = int(stdin.readline())   # total number of cases
for case in xrange(totalCases):
    key_max, key_n, alpha_n = stdin.readline().rstrip().split()
    key_f = stdin.readline().rstrip().split()
    
    cases.append([(int(key_max), int(key_n), int(alpha_n)), key_f])

# print cases
n = 1	# case number
for case in cases:
	key_max, key_n, alpha_n = case[0]
	key_f = case[1]
	key_f = [int(i) for i in key_f]
	key_f.sort()
	key_f.reverse()
	
	key_n = key_n
	counter = 0
	keyPresses = 0
	for i in key_f:
		keyPresses = keyPresses + (int(i) * ((counter / key_n) + 1))
		counter = counter + 1
	
	print "Case #%s: %s" % (n, keyPresses)
	
	n = n + 1

