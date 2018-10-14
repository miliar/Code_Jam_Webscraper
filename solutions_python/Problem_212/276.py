import sys
import math
import time


def f(p, gs):
    mods = [0]*p
    
    for g in gs:
        mods[g%p] += 1

    if p == 2:
        return int(mods[0] + math.ceil(mods[1]/2))

    elif p == 3:
        a = min(mods[1], mods[2])
        mods[1] -= a
        mods[2] -= a

        return int(mods[0] + a + mods[1]//3 + mods[2]//3 +
                (1 if mods[1]%3 != 0 or mods[2]%3 != 0 else 0))
    
    else:
        assert p == 4
        
        a = min(mods[1], mods[3])
        b = mods[2]//2

        mods[1] -= a
        mods[3] -= a
        mods[2] -= b*2
        assert mods[2] == 0 or mods[2] == 1

        ans = mods[0] + a + b

        c = mods[1] if mods[1] > 0 else mods[3]

        if mods[2] == 1 and c >= 2:
            c -= 2
            ans += 1

        ans += math.ceil(c/4)

        return int(ans)

        
        



numOfTestCase = int(input())
t0 = time.time()

for testCase in range(numOfTestCase):
    n, p = map(int, input().split())
    gs = list(map(int, input().split()))

    assert p >= 2
    assert p <= 4
    assert len(gs) == n

    t1 = time.time()

    print('Case #' + str(testCase+1) + ':', f(p, gs))

    if numOfTestCase >= 10:
        t2 = time.time()
    
        print('... #' + str(testCase+1) + '/' + str(numOfTestCase),
              '{0:.2f}'.format(t2 - t1),
              '{0:.2f}'.format(t2 - t0),
              file=sys.stderr)
    
