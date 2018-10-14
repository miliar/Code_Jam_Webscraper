def solve(C, F, X):
    def timeToCompletion(nFarms, target):
        return target/(2.+nFarms*F)

    if X <= C:
        return X / 2.

    nFarms = int((X*F - 2*C - C*F)/(C*F) + 1.)
    #print nFarms
    #print [timeToCompletion(n, C) for n in range(nFarms)]
    prevT = sum([timeToCompletion(n, C) for n in range(nFarms)]) + timeToCompletion(nFarms, X)
    return prevT

for _t in range(int(raw_input())):
    C, F, X = map(float, raw_input().strip().split())
    print "Case #%d: %.7f" % (_t + 1, solve(C, F, X))
