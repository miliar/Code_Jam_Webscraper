#! /usr/bin/env python2
T = int(raw_input())
for t in xrange(1, T + 1):
    n = int(raw_input()) - 1
    table1 = [raw_input(), raw_input(), raw_input(), raw_input()]
    m = int(raw_input()) - 1
    table2 = [raw_input(), raw_input(), raw_input(), raw_input()]
    intersection = set(table1[n].split()) & set(table2[m].split())
    if len(intersection) == 0:
        print "Case #{}: Volunteer cheated!".format(t)
    elif len(intersection) > 1:
        print "Case #{}: Bad magician!".format(t)
    else:
        print "Case #{}: {}".format(t, intersection.pop())
