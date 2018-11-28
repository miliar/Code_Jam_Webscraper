from sys import stdin

def solve(t):
    line = stdin.readline().split(' ')
    n = int(line[0])
    p = int(line[1])

    line = stdin.readline().split(' ')

    odd = 0
    even = 0
    r1 = 0
    r2 = 0
    r3 = 0

    for i in range(0, n):
        g = int(line[i])
        if p == 2:
            if g % 2 == 0:
                even += 1
            else:
                odd += 1
        elif p == 3:
            if g % 3 == 0:
                even += 1
            elif g % 3 == 1:
                r1 += 1
            else:
                r2 += 1
        else:
            if g % 4 == 0:
                even += 1
            elif g % 4 == 1:
                r1 += 1
            elif g % 4 == 2:
                r2 += 1
            else:
                r3 += 1

    if p == 2:
        res = even + (odd // 2) + (odd % 2)
    elif p == 3:
        res = even
        if r1 > r2:
            res += r2
            dif = r1 - r2
        else:
            res += r1
            dif = r2 - r1
        res += (dif // 3)
        if dif % 3 != 0:
            res += 1
    else:
        res = even + (r2 // 2)
        if r1 > r3:
            res += r3
            dif = r1 - r3
        else:
            res += r1
            dif = r3 - r1
        res += (dif // 4)
        if r2 % 2 == 0:
            # Only 1 or 3 left
            if dif % 4 != 0:
                res += 1
        else:
            if (dif % 4) > 2:
                res += 2
            else:
                res += 1


    print('Case #' + str(t + 1) + ': ' + str(res))

T = int(stdin.readline())
for t in range(0, T):
    solve(t)
