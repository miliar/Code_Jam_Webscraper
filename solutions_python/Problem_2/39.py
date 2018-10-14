def mktime(s, t):
    h, m = (int(x) for x in s.split(':'))
    t = h*60+m+t
    return '%02d:%02d' % (t // 60, t % 60)

def cmp_ev(a, b):
    c = cmp(a['time'], b['time'])
    if c == 0:
        c = cmp(a['event'], b['event'])
    return c

def run_case():
    turnaround = int(input())
    NA, NB = (int(x) for x in input().split())
    events = []

    for _ in range(NA):
        ta, tb = input().split()
        ta = mktime(ta, 0)
        tb = mktime(tb, turnaround)
        events.append({'station': 'A', 'event': 'departure', 'time': ta})
        events.append({'station': 'B', 'event': 'arrival', 'time': tb})

    for _ in range(NB):
        ta, tb = input().split()
        ta = mktime(ta, 0)
        tb = mktime(tb, turnaround)
        events.append({'station': 'B', 'event': 'departure', 'time': ta})
        events.append({'station': 'A', 'event': 'arrival', 'time': tb})

    events.sort(cmp_ev)

    stations = {}
    result = {}
    stations['A'] = 0
    stations['B'] = 0
    result['A'] = 0
    result['B'] = 0

    for x in events:
        s = x['station']
        e = x['event']

        if e == 'departure':
            if stations[s] == 0:
                result[s] += 1
            else:
                stations[s] -= 1

        elif e == 'arrival':
            stations[s] += 1
    
    return result['A'], result['B']


def main():
    N = int(input())
    for i in range(N):
        ra, rb = run_case()
        print('Case #%d: %d %d' % (i+1, ra, rb))


main()
