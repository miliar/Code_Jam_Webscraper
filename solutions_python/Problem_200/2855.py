def tidy(n):
    for j in range(len(n) - 1, 0, -1):
        curInt = n[j]
        prevInt = n[j - 1]
        if (prevInt > curInt):
            # if (prevInt == 1):
            #     n[j-1] = 0
            #
            # elif (j == lengthInt):
            #     n[j] = 9
            # else:
            #     n[j] = n[j + 1]
            for k in range((j), len(n)):
                n[k] = 9
            newInt = prevInt - 1
            newInt = 9 if newInt < 0 else newInt
            n[j - 1] = newInt
    return int(''.join(map(str,n)))


t = int(input())
for i in range(1, t+1):
    n = [int(v) for v in input()]
    lengthInt = len(n) - 1
    if (lengthInt == 0):
        print("Case #{}: {}".format(i, n[0]))
    else:
        newList = tidy(n)
        print("Case #{}: {}".format(i, newList))



