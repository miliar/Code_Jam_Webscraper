#!/usr/bin/python

cases = int(raw_input())
for case in range(1,cases+1):
    N = int(raw_input())
    windows = []
    for i in range(N):
        A, B = map(int, raw_input().split())
        windows.append( (A, B) )
    # Now compute intersections
    points = 0
    for i in range(N):
        A, B = windows[i]
        for j in range(N):
            if i == j:
                continue
            C, D = windows[j]
            # Only count intersections where the 2nd rope
            # crosses the first from bottom to top
            # This prevents counting the same intersection twice
            if C < A and D > B:
                points += 1

    print 'Case #%d: %d' % (case, points)
