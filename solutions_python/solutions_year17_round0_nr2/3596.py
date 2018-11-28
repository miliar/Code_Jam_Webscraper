def getNextLargestTidy(s, length):
    curr = int(s[0])
    first = True
    idx = -1
    res = ''
    for i, n in enumerate(s[1:]):
        n = int(n)
        if n == curr and first:
            idx = i
            first = False
        if n < curr:
            if first:
                idx = i
            digit = int(s[idx]) - 1
            res = s[:idx] + str(digit) + '9' * (length - idx - 1)
            break
        if i == length - 2:
            res = s
            break
        curr = n
    res = res.lstrip('0') or '0'
    return res


cases = int(input())
for c in range(1, cases + 1):
    s = input()
    length = len(s)
    res = ''
    if length < 2:
        res = s
    else:
        res = getNextLargestTidy(s, length)
    print("Case #{}: {}".format(c, res))
