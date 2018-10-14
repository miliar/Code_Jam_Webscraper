#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(problem):
    friends = 0
    standing = 0
    max_shyness, members = problem.split()
    for level in xrange(0, int(max_shyness) + 1):
        if members[level] != 0 and standing < level:
            friends = friends + (level - standing)
            standing = level + int(members[level])
        else:
            standing = standing + int(members[level])
    return friends

if __name__ == "__main__":
    testcases = input()
     
    for caseNr in xrange(1, testcases+1):
        problem = raw_input()
        print("Case #%i: %s" % (caseNr, solve(problem)))
