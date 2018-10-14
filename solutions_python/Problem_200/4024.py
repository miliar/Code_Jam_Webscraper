def small():
    t = int(input())

    if t >= 1 and t <= 100:
        for i in range(1, t + 1):
            n = int(input())
            if n >= 1 and n <= 1000:
                lastOrderNumber = 0
                for x in range(0, n + 1):
                    # print("x: {}".format(x))
                    if  verifyOrderNumber(x):
                        lastOrderNumber = x
                print("Case #{}: {}".format(i, lastOrderNumber))


def verifyOrderNumber(n):
    res = True
    stringNumbers = str(n);
    before = int(stringNumbers[0])
    for digit in stringNumbers:
        if int(digit) >= before:
            before = int(digit)
        else:
            res = False
            break
    return res


small()
