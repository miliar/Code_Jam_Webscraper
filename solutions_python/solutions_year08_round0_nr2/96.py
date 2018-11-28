import sys

debug = False

def handle_event(time):
    if debug : print time, events[time]
    for type,station in sorted(events[time]):
        if type == 'arrival':
            handle_arrival(station)
        else:
            handle_departure(station)
        if debug : print orig, actual

def handle_arrival(station):
    if debug : print 'Train arrives at',station,'station.'
    actual[station] += 1

def handle_departure(station):
    if debug : print 'Train leaves', station, 'station.'
    if actual[station] > 0 :
        actual[station] -= 1
    else:
        orig[station] += 1

def read_test_case(lines):
    t = int(lines[0].strip())
    na, nb = lines[1].strip().split()
    na, nb = int(na), int(nb)
    for line in lines[2:2+na]:
        td, ta = line.strip().split()
        hours, minutes = int(ta[0:2]), int(ta[3:])
        ta = '%02d' % (hours + (minutes+t)/60) + ':%02d' % ((minutes+t)%60)
        if not (td in events) : events[td] = []
        if not (ta in events) : events[ta] = []
        events[td] += [('departure', 'a')]
        events[ta] += [('arrival', 'b')]
    for line in lines[2+na:2+na+nb]:
        td, ta = line.strip().split()
        hours, minutes = int(ta[0:2]), int(ta[3:])
        ta = '%02d' % (hours + (minutes+t)/60) + ':%02d' % ((minutes+t)%60)
        if not (td in events) : events[td] = []
        if not (ta in events) : events[ta] = []
        events[td] += [('departure', 'b')]
        events[ta] += [('arrival', 'a')]
    return lines[2+na+nb:]

lines = [l for l in open(sys.argv[1])]

cases = int(lines[0])
lines = lines[1:]

for case in xrange(cases):
    events = {}
    actual = {'a':0,'b':0}
    orig = {'a':0,'b':0}
    lines = read_test_case(lines)
    for time in sorted(events.keys()):
        handle_event(time)
    print 'Case #'+str(case+1)+':', orig['a'], orig['b']
    if orig['a'] + orig['b'] != actual['a'] + actual['b'] : 3/0
