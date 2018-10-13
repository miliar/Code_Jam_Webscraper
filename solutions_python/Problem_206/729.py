
def f(d, n, horses):
    max_time = None
    for (start, speed) in horses:
        time = float(d - start) / speed
        if max_time == None or time > max_time:
            max_time = time
        # print start, speed, time
    return d/max_time





t = int(raw_input())
for i in xrange(1, t+1):
    d, n = [int(x) for x in raw_input().split(' ')]
    horses = []
    for j in xrange(n):
        start, speed = [int(x) for x in raw_input().split(' ')]
        horses.append((start, speed))
    print 'Case #{}: {}'.format(i, f(d, n, horses))
