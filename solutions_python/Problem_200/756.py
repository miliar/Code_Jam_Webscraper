import numpy as np


def solve(d):
    for i in xrange(d, -1, -1):
        if is_good(i):
            return i
    return 0


def is_good(d):
    s = str(d)
    for i in xrange(1, len(s)):
        if s[i] < s[i-1]:
            return False
    return True


import itertools as it

def checker(s):
    ss = [int(c) for c in str(s)]

    check = lambda x: [x - y >= 0 for x, y in zip(x[1:], x)]
    min_sub = lambda x: x[:1 + len(list(it.takewhile(lambda y: y[0] - y[1] >= 0, zip(x[1:], x))))]
    rest = lambda x: x[1 + len(list(it.takewhile(lambda y: y[0] - y[1] >= 0, zip(x[1:], x)))):]

    result = []

    while len(rest(ss)) > 0:
        tail = len(rest(ss))
        # print(tail)
        for i in range(tail):
            result.append(9)
        ss = ss[:-tail]
        ss[-1] -= 1

    return  ''.join(list(it.dropwhile(lambda x: x == '0', (list(map(str, ss + result))))))


def stress_test(N):
    cnt = 0
    while True:
        print cnt
        cnt += 1
        d = np.random.randint(low=1, high=N+1)
        x1 = solve(d)
        x2 = checker(d)
        if int(x1) != int(x2):
            print d, x1, x2
            raise
        


for qq in xrange(1, int(raw_input())+1):
    d = int(raw_input())
    ans = checker(d)
    print 'Case #{}: {}'.format(qq, ans)
