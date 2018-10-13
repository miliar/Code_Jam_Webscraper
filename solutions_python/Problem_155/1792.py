#!/usr/bin/env python

def solve(max_s, s_list):
    #print "%d" % max_s
    standing = int(s_list[0])
    required = 0
    needed = 0
    for char in s_list[1:]:
        required += 1
        num = int(char)
        if num:
            if standing < required:
                needed += required - standing
                standing = required
            standing += num
    return needed
            
        

for case in xrange(int(raw_input())):
    print "Case #%d:" % (case+1),
    max_s, s_list = raw_input().split()
    print solve(int(max_s), s_list)
