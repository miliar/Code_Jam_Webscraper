#!/usr/bin/python

import sys

def readline():
	return sys.stdin.readline()

def readint():
	return int(readline())

def readtestcase():
	testcase_string = readline()
	[_, shyness] = testcase_string.split(" ")
	return list(map(int, shyness.strip()))

def simulate(shyness):
	standing = 0
	friends = 0
	for shyness, cnt in enumerate(shyness):
		new_friends = 0
		if standing < shyness:
			new_friends += shyness - standing
		standing += cnt + new_friends
		friends += new_friends
	return friends

num_testcases = readint()
for i in range(num_testcases):
	shyness = readtestcase()
	print('Case #' + str(i+1) + ': ' + str(simulate(shyness)))
