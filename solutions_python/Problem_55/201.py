# Google CodeJam, Qualification Round 2010, Problem C - sj26@sj26.com
# This really should be optimized.
import sys
lines = (len(sys.argv) > 1 and open(sys.argv[1]) or sys.stdin).xreadlines()
tests_len = int(lines.next().strip())
for tests_num in xrange(0, tests_len):
    circuits, capacity, groups_len = map(int, lines.next().strip().split())
    groups = map(int, lines.next().strip().split())
    sys.stderr.write('Test #%d: %dx%d, %r;' % (tests_num + 1, circuits, capacity, groups))
    earnings = 0
    circuit = 0
    while circuit < circuits:
        circuit += 1
        take = 1
        while take < groups_len and sum(groups[:take + 1]) <= capacity:
            take += 1
        earnings += sum(groups[:take])
        groups = groups[take:] + groups[:take]
    sys.stderr.write(' %d.\n' % (earnings,))
    print 'Case #%d: %d' % (tests_num + 1, earnings)