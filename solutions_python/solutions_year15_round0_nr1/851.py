#!/usr/bin/env python
T = input()
for t in range(T):
    line = raw_input().split()
    smax = int(line[0])
    shyness = map(int, line[1])
    count = 0
    needed = 0
    for i in range(len(shyness)):
        if count < i:
            needed += i - count
            count  = i
        count += shyness[i]
    print 'Case #%d: %d' % (t + 1, needed)
