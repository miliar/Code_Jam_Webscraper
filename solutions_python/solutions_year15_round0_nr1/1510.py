#!/bin/env python2

tests = input()

for test in range(tests):
    line = raw_input().split(' ')[1]
    people = []
    for num in line:
        people.append(int(num))
    standing = 0
    added = 0
    for i, num in enumerate(people):
        if i > standing:
            added += (i - standing)
	    standing += (i - standing)
        standing += num
    print "Case #{0}: {1}".format(test+1, added)
