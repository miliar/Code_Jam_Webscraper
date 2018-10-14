#!/usr/bin/python

for case in range(input()):
    N = input()
    ropes = []
    cross = 0
    for i in range(N):
        points = map(int, raw_input().split())
        for rope in ropes:
            if (rope[0] < points[0]) and (rope[1] > points[1]):
                cross += 1
            elif (rope[0] > points[0]) and (rope[1] < points[1]):
                cross += 1

        ropes.append(points)
    print 'Case #%s: %d' % (case + 1, cross)
