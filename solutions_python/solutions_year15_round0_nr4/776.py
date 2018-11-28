#!/usr/bin/python

import sys

G='GABRIEL'
R='RICHARD'

map = {
'211' : R,
'212' : G,
'213' : R,
'214' : G,
'222' : G,
'223' : G,
'224' : G,
'233' : R,
'234' : G,
'244' : G,
'311' : R, 
'312' : R,
'313' : R,
'314' : R,
'322' : R,
'323' : G,
'324' : R,
'333' : G,
'334' : G,
'344' : R,
'411' : R, 
'412' : R,
'413' : R,
'414' : R,
'422' : R,
'423' : R,
'424' : R,
'433' : R,
'434' : G,
'444' : G,
}

infile=sys.argv[1]

lines = [line.strip() for line in open(infile)]
num_cases=int(lines[0])

for case in xrange(1, num_cases+1):
    line = [int(i) for i in lines[case].split()]
    if(line[0] == 1):
        print "Case #" + str(case) + ": " + G
    else:
        if(line[1] > line[2]):
            tmp = line[1]
            line[1] = line[2]
            line[2] = tmp
        key=''.join(str(e) for e in line)
        if key in map:
            print "Case #" + str(case) + ": " + map[key]
        else:
            raise Exception("invalid entry")
