def can_be_done (x, r, c):
    # because one of the pieces has a hole, that cannot be filled
    if x >= 7:
        return False

    # check multiplicity
    if r * c % x != 0:
        return False

    # check if all the L-shaped pieces fit (because they maximise one dimension once we fix the other one)
    for i in range(1, x+1):
        j = x + 1 - i
        if (i > r or j > c) and (j > r or i > c):
            return False

    # there's a margin of 1 around any possible piece: always possible
    for i in range(1, x+1):
        j = x + 1 - i
        if (i+2 <= r and j+2 <= c) or (j+2 <= r and i+2 <= c):
            return True

    # possible shapes are so simple it's always possible
    if x <= 3:
        return True

    # remaining cases:
    if x == 4 and (r == 2 or c == 2):
        # the S shaped piece obstructs the square and leaves an odd number of cells on each side
        return False

    if x == 4:
        # remains 3x4 and 4x4: always possible
        return True

    if r == 3 or c == 3:
        # the W shape causes problems for X=5, and a similar one for X=6
        return False

    return True

import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    x, r, c = tuple(int(x.strip()) for x in sys.stdin.readline().strip().split())
    print("Case #%d: %s" % (i+1, "GABRIEL" if can_be_done(x,r,c) else "RICHARD"))
