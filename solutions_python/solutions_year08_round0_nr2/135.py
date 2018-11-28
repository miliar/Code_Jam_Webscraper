import bisect

def clock_to_number(clock):
    hour, minute = map(int, clock.split(':'))
    return hour * 60 + minute

import sys
f = sys.stdin
n = int(f.readline())
for case in range(1, n+1):
    t = int(f.readline())
    na, nb = map(int, f.readline().split())
    all_trip = []
    for i in range(na):
        departure, arrival = map(clock_to_number, f.readline().split())
        all_trip.append((departure, 'ab', arrival))
    for i in range(nb):
        departure, arrival = map(clock_to_number, f.readline().split())
        all_trip.append((departure, 'ba', arrival))
    arrival_at_a = []
    arrival_at_b = []
    from_a = 0
    from_b = 0
    all_trip.sort()
    for departure, kind, arrival in all_trip:
        if kind == 'ab':
            if arrival_at_a and arrival_at_a[0] + t <= departure:
                del arrival_at_a[0]
            else:
                from_a += 1
            bisect.insort(arrival_at_b, arrival)
        if kind == 'ba':
            if arrival_at_b and arrival_at_b[0] + t <= departure:
                del arrival_at_b[0]
            else:
                from_b += 1
            bisect.insort(arrival_at_a, arrival)
    print 'Case #%d: %d %d' % (case, from_a, from_b)
