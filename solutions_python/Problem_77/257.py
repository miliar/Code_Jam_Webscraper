from codejam import *

@memoized
def GSort(n):
    if n < 2: return 0.0
    return n

@main
def GoroSort():
    T = read_int()
    for case in xrange(T):
        N = read_int()
        init = [0] + read_ints()
        counted = [False] * len(init)
        debug(init[1:])
        result = 0
        for i,n in enumerate(init):
            if not i: continue
            if not counted[i]:
                j = i
                n = 1
                while init[j] != i:
                    j = init[j]
                    counted[j] = True
                    n += 1
                g = GSort(n)
                result += g
                debug((result, n, g))
        printcase(case, '%.6f' % result)
