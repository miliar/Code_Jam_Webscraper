t = int(raw_input())

for i in xrange(t):
    n = int(raw_input())

    digits = [int(d) for d in str(n)]
    result = [int(d) for d in str(n)]

    remove_first = False
    index = 0

    for j in xrange(len(digits) - 1):
        if digits[j] > digits[j + 1]:
            result[j] = (digits[j] - 1) % 10
        
            if (result[j] == 0):
                result[j] = 9
                remove_first = True

            for k in xrange(j + 1, len(digits)):
                result[k] = 9

            index = j

            for k in reversed(xrange(1, j + 1)):
                if (result[k] < result[k - 1] or remove_first):
                    result[k - 1] = 9 if remove_first else result[k]

            break

    if (remove_first):
        result[0] = 0
        r = int(''.join(map(str, result)))
    else:
        r = int(''.join(map(str, result)))

        for k in reversed(xrange(1, index + 1)):
            result[k] = result[k + 1]
            r2 = int(''.join(map(str, result)))

            if r2 <= n:
                r = r2

    print 'Case #' + str(i + 1) + ':', r