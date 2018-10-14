remember = {}

import itertools

def at_least_p(p, total, surprising):
    global remember
    key = str(total) + str(surprising) + str(p)
    if key in remember:
        return remember[key]
    step = 1
    if surprising:
        step = 2
    for m in xrange(0, 11):
        for n in xrange(max(0, m - step), min(11, m + step + 1)):
            for o in xrange(max(0, m - step, n - step), min(11, m + step + 1, n + step + 1)):
                if m + n + o == total and (m >= p or n >= p or o >= p):
                    remember[key] = True
                    return True
    remember[key] = False
    return False


N = int(raw_input())

for case in xrange(0, N):
    numbers = map(int, raw_input().split(" "))
    googlers = numbers[0]
    surprising = numbers[1]
    p = numbers[2]
    results = numbers[3:]

    base = [True] * surprising + [False] * (googlers - surprising)
    permutations = list(itertools.permutations(base, len(base)))

    best = 0

    for sample in permutations:
        L = len(results)
        at_least = 0
        for u in range(0, L):
            x = results[u]
            if at_least_p(p, x, sample[u]):
                at_least = at_least + 1
        if at_least > best:
            best = at_least
    print "Case #" + str(case + 1) + ": " + str(best)
            


