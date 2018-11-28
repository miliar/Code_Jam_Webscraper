#!/bin/env python
#-*- coding: utf_8 -*-


###########
# imports #
###########
import math


#############
# constants #
#############
DEBUG = False


#############
# functions #
#############
def remove_zero (num):
	begin = -1
	for i in range (len (num) - 1):
		if num[i] != '0':
			begin = i
			break
	return num[begin:] if begin > 0 else num


def get_squares (low, high):
	left_bound = int (math.sqrt (low))
	if left_bound * left_bound < low:
		left_bound += 1
	right_bound = int (math.sqrt (high))
	if right_bound * right_bound > high:
		right_bound -= 1
	if DEBUG: print >> sys.stderr, 'left: %d, right: %d' % (left_bound, right_bound)
	for i in range (left_bound, right_bound + 1):
		if is_fair (str (i)):
			yield str (i * i)


def is_fair (num):
	for i in range (len (num) / 2):
		if num[i] != num[-i-1]:
			return False
	return True


########
# main #
########
import sys
if len (sys.argv) > 1:
	sys.stdin = open (sys.argv[1], 'r')


for case in range (int (raw_input().strip())):
	case += 1
	low, high = map (lambda x: int (remove_zero (x)), raw_input().rstrip().split())
	if DEBUG: print >> sys.stderr, '  '.join (get_squares (low, high))
	if DEBUG: print >> sys.stderr, filter (lambda x: is_fair (x), get_squares (low, high))
	if DEBUG: print >> sys.stderr
	print 'Case #%d: %d' % (case, len (filter (lambda x: is_fair (x), get_squares (low, high))))
