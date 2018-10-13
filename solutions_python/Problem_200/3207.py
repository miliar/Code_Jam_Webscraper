def get_max(top):
    last = 9
    result = []
    for j in [long(x) for x in reversed(str(top))]:
        if j > last:
            result = [9] * len(result)
            result.append(j - 1)
            last = j - 1
        else:
            result.append(j)
            last = j
    return long(''.join(map(str, reversed(result))))


n = long(input())
for i in range(n):
    test = long(input())
    prlong("Case #{}: {}".format(i + 1, get_max(test)))
