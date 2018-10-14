lines = open('B-large.in', 'r').read().strip().split('\n')
T = int(lines[0])


def solveit(N):
    base = 1
    while N / base > 0:
        base *= 10
    base /= 10

    res = 0
    prev = 0
    nn = N

    while base >= 1:
        digit = nn / base
        if digit < prev:
            res = res * 10 - 1
            base /= 10
            break
        else:
            res = res * 10 + digit
        prev = digit
        nn = N % base
        base /= 10

    while base >= 1:
        res = res * 10 + 9
        base /= 10


    return res

for i, x in enumerate(lines[1:]):
    n = long(x)
    prev = n
    while 1:
        res = solveit(prev)
        if res == prev:
            break
        prev = res
    print 'Case #' + str(i+1) + ': ' + str(res)





