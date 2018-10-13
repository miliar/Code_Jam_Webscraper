from fileinput import input
import math


def tidy(num, tidies):
    n = int(math.log10(num)) + 1
    while True:
        if num in tidies:
            return num

        res = True
        tmp = num
        _d = 9
        i = 0
        while tmp > 0:
            tmp, d = divmod(tmp, 10)
            if _d >= d:
                _d = d
                i += 1
            else:
                res = False
                break

        if not res:
            num -= int(math.pow(10, i))

            if num == 0:
                return '9' * (n-1)
            else:
                cool = num
                for j in range(i):
                    d = cool // 10**j % 10
                    num -= (d * int(math.pow(10, j)))
                    num += (9 * int(math.pow(10, j)))

        else:
            tidies.add(num)
            return str(num)


case = 1
tidies = set([9])
for _ in range(int(raw_input())):
    num = int(raw_input())
    if len(str(num)) == 1:
        sol = num
    else:
        sol = tidy(num, tidies)

    print 'Case #{0}: {1}'.format(case, sol)
    case += 1
