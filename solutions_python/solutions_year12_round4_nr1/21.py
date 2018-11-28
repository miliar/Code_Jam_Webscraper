import sys
from collections import deque

casenum = 1
def doit():
    global lines
    global casenum

    N = int(lines.popleft())

    vines = []

    for i in range(N):
        d, l = map(int, lines.popleft().split(" "))
        vines.append({
            'd' : d,
            'l' : l,
            'el': 0
        })

    vines.sort(key=lambda x: x['d'])

    D = int(lines.popleft())

    # Add a dummy vine to see if the dest is reachable
    vines.append({'d': D, 'l' : 1, 'el' : 0})

    # First vine's effective length is how far away it is
    vines[0]['el'] = vines[0]['d']

    ans = "YES"

    for i in range(1, len(vines)):
        # Determine vine i's effective length
        this_vine = vines[i]
        best = 0
        for j in range(i):
            prev_vine = vines[j]

            # Can't reach
            if prev_vine['el'] < this_vine['d'] - prev_vine['d']:
                continue

            best = max(best, min(this_vine['d'] - prev_vine['d'], this_vine['l']))

        if best == 0:
            ans = "NO"
            break

        this_vine['el'] = best

    # print vines
    print 'Case #%d: %s' % (casenum, ans)
    casenum += 1

lines = deque([x.strip() for x in sys.stdin.readlines()])
ZZZ = int(lines.popleft())
for case in range(ZZZ):
    doit()
