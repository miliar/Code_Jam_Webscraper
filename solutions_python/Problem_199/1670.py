import numpy as np

ncases = input()

for c in xrange(ncases):
    pancakes, flip = raw_input().split()
    pancakes = np.asarray(map(lambda x: x == '+', pancakes))
    flip = int(flip)

    original = pancakes.copy()
    numpancakes = pancakes.size

    numflips = 0

    while np.sum(pancakes) != numpancakes:
        offset = np.where(~pancakes)[0][0]

        if offset + flip > numpancakes:
            numflips = 'IMPOSSIBLE'
            break

        pancakes[offset:offset+flip] = ~pancakes[offset:offset+flip]

        if np.count_nonzero(pancakes == original) == numpancakes:
            numflips = 'IMPOSSIBLE'
            break

        numflips += 1

    print 'Case #%d: %s' % (c + 1, numflips)
