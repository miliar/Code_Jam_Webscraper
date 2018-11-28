#!/usr/bin/env python

T = int(raw_input())
for t in xrange(T):
    answer1 = int(raw_input())
    cards1 = [map(int, raw_input().strip().split()) for i in xrange(4)]
    answer2 = int(raw_input())
    cards2 = [map(int, raw_input().strip().split()) for i in xrange(4)]

    set1 = set(cards1[answer1 - 1])
    set2 = set(cards2[answer2 - 1])
    chosen = set1.intersection(set2)

    print "Case #%d:" % (t+1),
    if (len(chosen) == 1):
        print chosen.pop()
    elif (len(chosen) == 0):
        print "Volunteer cheated!"
    else:
        print "Bad magician!"

