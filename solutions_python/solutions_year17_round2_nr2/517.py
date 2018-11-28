from DomainModel.TestCase import TestCase


class R2B:
    def Solve(self):
        def l2(N, a):
            ret = ''
            if N % 2 != 0 or a[0][0] != a[1][0]:
                ret = 'IMPOSSIBLE'
            else:
                for i in range(a[1][0]):
                    ret += a[0][1]
                    ret += a[1][1]
            return ret

        def l3(N, a):
            if a[0][0] > a[1][0] + a[2][0]:
                ret = 'IMPOSSIBLE'

            df1 = a[0][0] - a[1][0]
            df2 = a[2][0] - df1
            ret = ''
            for i in range(df2):
                ret += a[0][1]
                ret += a[1][1]
                ret += a[2][1]
            for i in range(a[1][0] - df2):
                ret += a[0][1]
                ret += a[1][1]
            for i in range(df1):
                ret += a[0][1]
                ret += a[2][1]

            return ret

        def check(s):
            if s == 'IMPOSSIBLE':
                return True

            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    return False
            if s[0] == s[-1]:
                return False
            return True

        tests = int(input())
        for test in range(tests):
            N, R, O, Y, G, B, V = list(map(int, input().split()))
            a = [[R, 'R'], [B, 'B'], [Y, 'Y']]
            a = list(filter(lambda x: x[0] > 0, a))
            a.sort(reverse=True)
            ret = ''

            if len(a) <= 1:
                ret = 'IMPOSSIBLE'
            elif len(a) == 2:
                ret = l2(N, a)
            else:
                ret = l3(N, a)

            assert check(ret)

            print("Case #{}: {}".format(test + 1, ret))

    def Tests(self):
        yield TestCase("""5
6 2 0 2 0 2 0
3 1 0 2 0 0 0
6 2 0 1 1 2 0
4 0 0 2 0 0 2 
4 2 0 0 0 2 0
""", """Case #1: RYBRBY
Case #2: IMPOSSIBLE
Case #3: YBRGRB
Case #4: YVYV
Case #5: RBRB
""")
