#!/usr/bin/python
import sys



def solve(s, n):
    substrings = 0
    last_success_begin = -1
    streak_begin = 0
    streak_length = 0
    for c in xrange(len(s)):
        end = c + 1
        ch = s[c]
        if ch in 'aeiou':
            streak_length = 0
        else: # consanant
            streak_length += 1
            if streak_length >= n:
                last_success_begin = end - n
        if last_success_begin != -1:
            substrings += last_success_begin + 1
    return substrings

T = int(sys.stdin.readline())
for test_case in xrange(1, T+1):
    s, nstr = sys.stdin.readline().split()
    n = int(nstr)
    print "Case #{0}: {1}".format(test_case, solve(s,n))

"""    
print solve("quartz",3)
print solve("straight", 3)
print solve("gcj", 2)
print solve("tsetse", 2)
"""
