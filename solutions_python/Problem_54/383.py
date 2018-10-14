# Google CodeJam, Qualification Round 2010, Problem B - sj26@sj26.com
import sys
from fractions import gcd
from itertools import *
lines = (len(sys.argv) > 1 and open(sys.argv[1]) or sys.stdin).xreadlines()
tests_len = int(lines.next().strip())
for tests_num in xrange(1, tests_len + 1):
    # Parse events
    events = imap(int, lines.next().strip().split())
    events_len = events.next()
    events = list(events)
    events.sort()
    sys.stderr.write('Test #%d: %r;' % (tests_num, events))
    
    # Normalise events to immediately prior event (sorted)
    events_normalised = list(events[i] - events[0] for i in xrange(0, len(events)))
    sys.stderr.write(' %r;' % (events_normalised,))
    
    # Find the common GCD
    # Special case for gcd(0, 0) given event normalisation
    events_gcd = max(1, reduce(gcd, imap(gcd, islice(events_normalised, 1, None), iter(events_normalised))))
    sys.stderr.write(' %r;' % (events_gcd,))
    
    # Find the point in the future (or now) which is (last event + (n * events_gcd))
    future = 0
    future_offset = events[0] % events_gcd
    if future_offset > 0:
        future = events_gcd - future_offset
    sys.stderr.write(' %r.\n' % (future,))
    
    print 'Case #%d: %d' % (tests_num, future)