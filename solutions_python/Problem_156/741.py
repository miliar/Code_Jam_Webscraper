import sys
sys.setrecursionlimit(1000000)


def cookie(c):
    m = max(c)
    res = m
    for i in range(1, m+1):
        s = i
        for j in range(len(c)):
            if c[j] > i:
                if c[j] % i == 0:
                    s += c[j]/i - 1
                else:
                    s += c[j]/i
        res = min(res, s)
    return res


for i in range(input()):
    inpt = input()
    inpt = map(int, raw_input().split())
    print 'Case #' + str(i+1) + ': ' + str(cookie(inpt))
