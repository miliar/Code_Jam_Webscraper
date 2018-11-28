"""
Initial rate (r) = 2
In time t1, the number of cookies produced = 2t1
Farm can only be upgraded when cookie count reaches C. Time taken without upgrade = C/r.
To reach X, time taken with
No upgrade = X/2
1 upgrade = C/2 + X/(2 + F)
2 upgrades = C/2 + C/(2 + F) + X/(2 + 2F)
3 upgrades = C/2 + C/(2 + F) + C/(2 + 2F) + X/(2 + 3F)
.
.
n-1 upgrades = C/2 + C/(2+F) + C/(2 + 2F) + ...X/(2+(n-1)F)
n upgrades = C/2 + C/(2 + F) + C/(2 + 2F) + ... X/(2 + nF)
For nth upgrade to be fruitful,
C/(2 + (n-1)F) + X/(2 + nF) < X/(2 + (n-1)F)
C + X(2 + (n-1)F)(2 + nF) < X
4 + 4nF - 2F + n(n-1)F^2 < (X - C)/X
"""

import sys

with file(sys.argv[1]) as f:
    T = int(f.readline())
    for i in range(T):
        C, F, X = [float(n) for n in f.readline().strip().split()]
        bestTime = X / 2.0
        n = 1
        while True:
            newTime = bestTime - ((X - C)/ (2 + (n-1)*F)) + (X/(2 + n*F)) 
            if newTime >= bestTime:
                break
            bestTime = newTime
            n += 1
        print "Case #%d: %f" % (i+1, bestTime)
