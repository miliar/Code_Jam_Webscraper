#!/usr/bin/python

def time_to_min(s):
    a, b = s.split(':')
    return int(a)*60 + int(b)

def read():
    n = int(raw_input())
    cases = []
    for i in xrange(n):
        t = int(raw_input())
        na, nb = map(int, raw_input().split())
        atob = [ tuple(map(time_to_min, raw_input().split()))
                 for j in xrange(na) ]
        btoa = [ tuple(map(time_to_min, raw_input().split()))
                 for j in xrange(nb) ]
        cases.append( (t, atob, btoa) )
    return cases

def simulate():
    cases = read()

    # READY_* are intentionally less than LEAVE_*
    READY_A = 0
    READY_B = 1
    LEAVE_A = 2
    LEAVE_B = 3
    for i, (t, atob, btoa) in enumerate(cases):
        leave_a = [ (x[0], LEAVE_A)   for x in atob ]
        ready_b = [ (x[1]+t, READY_B) for x in atob ]
        leave_b = [ (x[0], LEAVE_B)   for x in btoa ]
        ready_a = [ (x[1]+t, READY_A) for x in btoa ]
        events = sorted(leave_a + ready_b + leave_b + ready_a)

        r_a = 0
        r_b = 0
        n_a = 0
        n_b = 0
        for time, ev in events:
            if ev == READY_A:
                r_a += 1
            elif ev == READY_B:
                r_b += 1
            elif ev == LEAVE_A:
                if r_a == 0:
                    n_a += 1
                else:
                    r_a -= 1
            elif ev == LEAVE_B:
                if r_b == 0:
                    n_b += 1
                else:
                    r_b -= 1
        print 'Case #%d: %d %d' % (i+1, n_a, n_b)


def main():
    simulate()


if __name__ == '__main__':
    main()
