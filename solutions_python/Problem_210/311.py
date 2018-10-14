import sys
from collections import namedtuple

Activity = namedtuple('Activity', ['p', 'c', 'd'])

def solve(activities):
    #print '======================================'
    exchanges = 0  # Number of times baby changed hands (minimize this)
    time = [0, 0]  # How much time parent i spend with baby
    buffer_time = 0  # How much time available without increasing exchanges
    slots = [[], []]  # Available time slots for parent i requiring exchange

    #print 'Activities: {}'.format(activities)
    for i in xrange(len(activities)):
        next = i + 1
        if i == len(activities) - 1:
            next = 0
        duration = activities[i].d - activities[i].c
        gap = activities[next].c - activities[i].d + (24*60 if next == 0 else 0)
        if activities[i].p != activities[next].p:
            #print '- Exchanging'
            exchanges += 1
            buffer_time += gap
            time[1 - activities[i].p] += duration
        else:
            #print '- Keeping'
            time[1 - activities[i].p] += duration + gap
            slots[activities[i].p].append(gap)

    #print 'Exchanges: {}, buffer: {}, time: {}, slots: {}'.format(exchanges, buffer_time, time, slots)

    diff = time[0] - time[1]
    # If we can handle it by moving current exchange we'll do that
    if abs(diff) <= buffer_time:
        #print '- solvable inside buffer time'
        return exchanges

    # Otherwise we have to introduce new exchanges
    p = 0 if diff > 0 else 1

    # Parent p has too much time
    t = time[p] - buffer_time
    #print 'Still needing {} minutes for parent {}'.format(t, p)
    for slot in sorted(slots[1 - p], reverse=True):
        #print 'Reducing with slot {}'.format(slot)
        t -= slot
        exchanges += 2
        if t <= 12*60:
            break

    return exchanges

t = int(sys.stdin.readline())
for i in xrange(1, t + 1):
    ac, aj = (int(i) for i in sys.stdin.readline().split())
    activities = []
    for _ in xrange(ac):
        c, d = (int(i) for i in sys.stdin.readline().split())
        activities.append(Activity(p=0, c=c, d=d))
    for _ in xrange(aj):
        c, d = (int(i) for i in sys.stdin.readline().split())
        activities.append(Activity(p=1, c=c, d=d))
    activities = sorted(activities, key=lambda a: a.c)
    exchanges = solve(activities)
    print 'Case #{}: {}'.format(i, exchanges)
