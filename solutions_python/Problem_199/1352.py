

def solve(s, k):
    i = 0
    flipped = False
    j = 0
    unflips = []
    flipsNeeded = 0
    while i < len(s):
        c = s[i]
        #print i, c

        while j < len(unflips) and unflips[j] <= i:
            # unflip
            flipped = not flipped
            j += 1

        if flipped:
            needsToFlip = c == '+'
        else:
            needsToFlip = c == '-'

        if needsToFlip:
            #print 'flipping'
            flipsNeeded += 1
            # Impossiboru
            if (i + k > len(s)):
                return None
            flipped = not flipped
            unflips.append(i + k)

        i += 1
    return flipsNeeded

import sys
lines = sys.stdin.readlines()

for i in range(1, len(lines)):
    l = lines[i].rstrip('\n')
    s, k = l.split(' ')
    r = solve(s, int(k))
    if r is None:
        rstr = 'IMPOSSIBLE'
    else:
        rstr = str(r)
    print 'Case #{}: {}'.format(i, rstr)
