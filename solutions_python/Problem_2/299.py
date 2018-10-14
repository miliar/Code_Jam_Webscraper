import sys

STATION_A = 0
STATION_B = 1

READY = 0
DEPART = 1

def print_events(events):
    for t, type, station in events:
        print '%02d:%02d %s %s' % (t / 60, t % 60,
                                   'A' if station == STATION_A else 'B',
                                   'D' if type == DEPART else 'R') 

def t(s):
    '''Convert 'hh:mm' to int(minutes after midnight)'''
    h, m = (int(c) for c in s.split(':'))
    return h * 60 + m

def solve(events):
    start_trains_a = 0
    start_trains_b = 0
    trains_a = 0
    trains_b = 0
    for t, type, station in events:
        if type == DEPART:
            if station == STATION_A and trains_a == 0:
                trains_a += 1
                start_trains_a += 1
            elif station == STATION_B and trains_b == 0:
                trains_b += 1
                start_trains_b += 1
            if station == STATION_A:
                trains_a -= 1
            else:
                assert(station == STATION_B)
                trains_b -= 1
        else:
            assert(type == READY)
            if station == STATION_A:
                trains_a += 1
            else:
                assert(station == STATION_B)
                trains_b += 1
                
    return start_trains_a, start_trains_b

def read_solve():
    '''Returns a list of events, (T, TYPE, STATION)'''
    turnaround = int(sys.stdin.readline())
    na, nb = (int(s) for s in sys.stdin.readline().split())
    events = []
    for station, n in [(STATION_A, na), (STATION_B, nb)]:
        for _ in xrange(n):
            depart, arrive = sys.stdin.readline().split()
            events.append((t(depart), DEPART, station))
            events.append((t(arrive) + turnaround,
                           READY,
                           STATION_A if station == STATION_B else STATION_B))
    events.sort()
    return solve(events)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in xrange(n):
        trains_a, trains_b = read_solve()
        print 'Case #%d: %d %d' % (i + 1, trains_a, trains_b)
