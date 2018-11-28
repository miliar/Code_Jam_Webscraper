#!/usr/bin/env python

cases = int(raw_input())
count = 1

while cases > 0:
    num_wires = int(raw_input())
    segments = []
    for _ in xrange(num_wires):
        ai, bi = map(int, raw_input().rstrip().split())
        segments.append((ai, bi))
    check_index = 0
    points = 0 
    while check_index < len(segments) - 1:
        a1 = segments[check_index][0]
        b1 = segments[check_index][1]
        for index in xrange(check_index+1, len(segments)):
            a2 = segments[index][0]
            b2 = segments[index][1]
            if (a1 < a2 and b1 > b2) or (a1 >a2 and b1 < b2):
                points += 1
        check_index += 1
    print "Case #%d: %d" %(count, points)
    count += 1
    cases -= 1
