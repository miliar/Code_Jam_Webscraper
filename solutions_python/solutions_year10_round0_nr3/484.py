#! /usr/bin/python
'''
Rollrcoastr
'''

T = int(raw_input())

for i in range(T):
    R, k, N = map(int, raw_input().split())
    money = 0
    oldpointer, newpointer = -1, 0
    groups = map(int, raw_input().split())
    for run in range(R):
        passengers = 0
        oldpointer = newpointer + len(groups)
        while True:
            # cant fit more people
            if groups[newpointer % len(groups)] > k - passengers:
                break
            # run out of people
            if newpointer == oldpointer:
                break
            # add them on
            passengers += groups[newpointer % len(groups)]
            money += groups[newpointer % len(groups)]
            newpointer += 1
    print 'Case #%d: %d' % (i + 1 , money)
