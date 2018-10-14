from DomainModel.TestCase import TestCase


class R2A:
    def Solve(self):
        tests = int(input())
        for test in range(tests):
            d, n = list(map(int, input().split()))
            mt = 0
            for i in range(n):
                kk, ss = list(map(int, input().split()))
                tt = (d - kk)/ss
                if tt>mt:
                    mt = tt
            v = d/mt
            print("Case #{}: {}".format(test+1,v))

    def Tests(self):
        yield TestCase("""3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10 
""", """Case #1: 101.000000
Case #2: 100.000000
Case #3: 33.333333
""")
