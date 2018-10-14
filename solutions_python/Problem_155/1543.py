#!/usr/bin/python

import sys

infile=sys.argv[1]

lines = [line.strip() for line in open(infile)]

num_cases=int(lines[0])

for case in xrange(1, num_cases+1):
    line = lines[case].split()
    smax = int(line[0])
    shyness = line[1]
    
    cur_standing = 0;
    num_friends = 0;
    for s in xrange(0, smax+1):
        num_people_waiting = int(shyness[s])
        if(cur_standing < s):
            needed = (s-cur_standing)
            num_friends = num_friends + needed 
            cur_standing = cur_standing + needed
        cur_standing = cur_standing + num_people_waiting 
    print "Case #" + str(case) + ":", num_friends
