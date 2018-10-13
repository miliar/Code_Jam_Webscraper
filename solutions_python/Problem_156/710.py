from sys import stdin, stdout

def solve_test_case(test_case_num):
    d = int(stdin.readline())
    a = map(int, stdin.readline().split())
    def can(x):
        b = a
        if not b:
            return True
        def can2(y):
            rt = x - y
            c = [z for z in b if z > rt]
            cnt = 0
            for z in c:
                cnt += (z - 1) / rt
            return cnt <= y

        for i in range(1, x):
            if can2(i):
                return True
        return False
    l = -1
    r = max(a)
    s = ''
    for i in range(r + 1):
        s += str(int(can(i)))
    while r - l > 1:
        m = (l + r) / 2
        if can(m):
            r = m
        else:
            l = m
    print 'Case #%d: %d' % (test_case_num, r)


t = int(stdin.readline())
for i in range(t):
    solve_test_case(i + 1)



