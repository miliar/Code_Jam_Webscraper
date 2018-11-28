from copy import deepcopy

def can(a, tm, was):
    if tm == 0:
        return max(a) == 0

    hs = ''.join(map(str, sorted(a))) + '--' + str(tm)
    if hs in was:
        return was[hs]

    nx = [max(0, x - 1) for x in a]
    if can(nx, tm - 1, was):
        print('Wait 1 minute')
        was[hs] = True
        return True

    for i in range(len(a)):
        x = a[i]
        for b in range(1, x // 2 + 1):
            nx = a[:i] + a[i + 1:] + [b, x - b]
            if can(nx, tm - 1, was):
                print('Split %d into %d and %d' % (x, b, x - b))
                was[hs] = True
                return True

    was[hs] = False
    return False


def stupid(n, a):
    for tm in range(1, 10):
        was = dict()
        if can(deepcopy(a), tm, was):
            return tm

for test in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = max(a)
    
    for mx in range(1, max(a)):
        steps = 0
        for x in a:
            steps += (x + mx - 1) // mx - 1
        ans = min(ans, steps + mx)

    print('Case #%d: %d' % (test + 1, ans))
