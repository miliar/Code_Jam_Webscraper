#! /usr/bin/env python

testfile = open("C-small-attempt2.in").read().split('\n')
num_cases = int(testfile[0])

for case in xrange(0,num_cases*2,2):
    line = testfile[case+1].split() + testfile[case+2].split()
    R, k = int(line[0]), int(line[1])
    groups = [int(x) for x in line[3:]]
    riders = []
    income = 0
    for ride in xrange(R):
        while sum(riders) < k and groups:
            if sum(riders) + groups[0] > k:
                 break
            riders.append(groups.pop(0))
        income += sum(riders)
        groups.extend(riders)
        riders = []
    print "Case #%s: %s" %(case/2+1, income)
