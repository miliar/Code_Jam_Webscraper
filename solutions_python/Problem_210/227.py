from DomainModel.TestCase import TestCase


class R3B:
    def Solve(self):
        tests = int(input())
        for test in range(tests):
            ret = 2
            na, nb = list(map(int, input().split()))
            la = []
            lb = []
            for i in range(na):
                f, t = list(map(int, input().split()))
                la.append((f, t))
            for i in range(nb):
                f, t = list(map(int, input().split()))
                lb.append((f, t))

            if na == 2 or nb == 2:
                l = la or lb
                l.sort()
                dt = l[1][1]-l[0][0]
                dt2 = (60*24-l[1][0]) + l[0][1]
                if dt>720 and dt2>720:
                    ret = 4



            print("Case #{}: {}".format(test + 1, ret))

    def Tests(self):
        yield TestCase("""5
1 1
540 600
840 900
2 0
900 1260
180 540
1 1
1439 1440
0 1
2 2
0 1
1439 1440
1438 1439
1 2
3 4
0 10
1420 1440
90 100
550 600
900 950
100 150
1050 1400
""", """Case #1: 2
Case #2: 4
Case #3: 2
Case #4: 4
Case #5: 6
        """)
