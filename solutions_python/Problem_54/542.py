#! /usr/bin/env python

testfile = open("input.in").read().split('\n')
num_cases = int(testfile[0])

def gcf(a,b):
    while b != 0:
        a, b = b, a % b
    return a

for case in xrange(num_cases):
    previous_events = testfile[case+1].split()[1:]
    previous_events = [int(x) for x in previous_events]
    mini = min(previous_events)
    previous_events = [x-mini for x in previous_events]
    previous_events.remove(0)
    gcf_of_list = reduce(gcf, previous_events)
    slarboseconds = ((mini+gcf_of_list-1)/gcf_of_list)*gcf_of_list-mini
    print "Case #%s: %s" %(case+1, slarboseconds)
