def tidy(numArr):
    for i in reversed(xrange(1, len(numArr))):
        if numArr[i] < numArr[i-1]:
            numArr[i-1] -= 1
            for j in xrange(i, len(numArr)):
                if numArr[j] == 9:
                    break
                numArr[j] = 9

    res = map(str, numArr)

    if numArr[0] != '0':
        return int(''.join(res))

    return int(''.join(res[1:]))

tc = int(raw_input())

for t in xrange(1, tc + 1):
    num = int(raw_input())
    res = tidy(map(int, str(num)))
    print "Case #{}: {}".format(t, res)