import numpy as np

ncases = input()

for c in xrange(ncases):
    N = input()
    numtidy = 0

    while N >= 0:
        tidy = True
        numtidy = N

        n = str(N)
        i = 0
        while tidy and i < len(n) - 1:
            if n[i] > n[i+1]:
                tidy = False
            i += 1

        if tidy:
            break
        else:
            n = str(N)
            N = n[:i-1] + str((int(n[i-1:i]) - 1) % 10) + '9' * (len(n[i+1:]) + 1)
            N = int(N)

    print 'Case #%d: %s' % (c + 1, numtidy)
