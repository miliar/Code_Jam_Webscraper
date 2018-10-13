from codejam import *

for case in xrange(readint()):
    inp = readintarray()
    N, s, p = inp[:3]
    scores = inp[3:]
    res = surprising = 0

    for score in scores:
        d, r = divmod(score, 3)
        if r == 0:
            pos = [
                [d, d, d],
                [d - 1, d + 1, d]
            ]
        elif r == 1:
            pos = [
                [d, d + 1, d],
                [d - 1, d + 1, d + 1]
            ]
        elif r == 2:
            pos = [
                [d + 1, d + 1, d],
                [d, d + 2, d]
            ]

        if any(n >= p for n in pos[0]):
            res += 1

        elif any(n >= p for n in pos[1]) and\
             not any(n < 0 for n in pos[1]):
            surprising += 1


    print "Case #%d: %d" % (case + 1, res + min(surprising, s))
