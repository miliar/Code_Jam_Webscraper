
#
# Google Code Jam 2010
# Qualification round: A. Snapper Chain
# submission by EnTerr
#

import sys

f = open(sys.argv[1])
def input(): return f.readline().strip();

for caseNo in xrange(1, int(input())+1):
    (N, K) = map(int, input().split())
    assert(N > 0)
    assert(K >= 0)
    # snapper chain described is like binary counter
    # and the lamp plugged into N-th snapper after K snaps is
    # ON iff all snappers before it are '1', i.e. '111....11'
    mask = (1 << N) - 1
    print 'Case #%d: %s' % (caseNo, 'ON' if (K & mask == mask) else 'OFF')

