from DomainModel.TestCase import TestCase


class R3A:
    def Solve(self):
        import itertools
        import math
        tests = int(input())
        for test in range(tests):
            n, k = list(map(int, input().split()))
            l = []
            for i in range(n):
                rx, hx = list(map(int, input().split()))
                l.append((rx, hx))
            l.sort(reverse=True, key=lambda x: (x[0], [1]))

            mS = 0
            for mr, mh in l:
                S = math.pi * mr * mr
                lh = list(filter(lambda y: y[0] <= mr, l))
                lh.sort(reverse=True, key=lambda y: y[1] * y[0])
                cnt = 0
                has = False
                if k > 1:
                    for r, h in lh:
                        S += math.pi * 2 * r * h
                        if r == mr and h == mh:
                            has = True
                        cnt += 1
                        if (cnt == k and has) or (cnt == k - 1 and not has):
                            break
                if not has:
                    S += math.pi * 2 * mr * mh
                    cnt += 1
                if cnt == k:
                    mS = max(S, mS)

            print("Case #{}: {}".format(test + 1, mS))

    def Tests(self):
        yield TestCase("""4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4
""", """Case #1: 138230.076757951
Case #2: 150796.447372310
Case #3: 43982.297150257
Case #4: 625.176938064
        """)
