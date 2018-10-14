ans = []
with open('input.txt') as fil:
    t = int(fil.readline())
    for i in range(t):
        c, f, x = map(float, fil.readline().split())
        def check(test):
            tm = 0.0
            y = 2.0
            for j in range(test):
                tm += c / y
                y += f
            tm += x / y
            return tm
        l, r = 0, (10**5)
        while r - l > 3:
            m1 = (l + l + r) // 3
            m2 = (l + r + r) // 3
            if check(m1) < check(m2):
                r = m2
            else:
                l = m1
        if (r == 10 ** 5):
            print('oops', i + 1);
        res = float('inf')
        for j in range(l, r):
            res = min(res, check(j))
        ans.append(res)
with open('output.txt', 'w') as f:
    for xn, x in zip(range(1, len(ans) + 1), ans):
        print('Case #%d: %.7f' % (xn, x), file=f)
