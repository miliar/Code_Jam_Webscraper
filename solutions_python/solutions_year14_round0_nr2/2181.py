import sys

fh = sys.stdin

cases = int(fh.readline())

for case in xrange(1, cases+1):
    building_cost, extra, goal = map(float, fh.readline().split())

    time = 0
    rate = 2
    while True: 
        if goal / (rate + extra) < (goal - building_cost) / rate:
            time += building_cost / rate
            rate += extra
        else:
            time += (goal / rate) 
            break

    print 'Case #{0}: {1:.7f}'.format(case, time) 
