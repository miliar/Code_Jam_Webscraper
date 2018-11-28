def isTidy(n):
    s = str(n)
    prev = 0
    for c in s:
        x = int(c)
        if x < prev:
            return False
        else:
            prev = x
    return True

def getDigit(n, position):
    s = str(n)
    return int(s[position])

def setDigit(n, position, to):
    s = list(str(n))
    s[position] = str(to)
    return int("".join(s))

def decreaseDigit(n, position):
    x = getDigit(n, position)
    x = x - 1
    if x == 0:
        x = 9
    return setDigit(n, position, x)

def lastTidyIndex(n):
    s = list(str(n))
    prev = 0
    for i, c in enumerate(s):
        c = int(c)
        if c < prev:
            break
        prev = c
    return i - 1

def getMaxDigitInRange(n, start, end):
    max_so_far = getDigit(n, start)
    for i in range(start+1, end+1):
        max_so_far = max(max_so_far, getDigit(n, i))
    return max_so_far

def findLargestTidyNumberBelow(n):
    if isTidy(n):
        return n

    l = lastTidyIndex(n)
    m = n
    for i in range(l+1, len(str(m))):
        m = setDigit(m, i, 9)

    max_digit = getDigit(m, l) - 1
    i = l
    while i >= 0:
        max_digit = min(max_digit, getDigit(n, i))
        if getDigit(m, i) > max_digit:
            m = setDigit(m, i, max_digit)
        if max_digit < getMaxDigitInRange(m, 0, i-1):
            m = setDigit(m, i, 9)
        i = i - 1
    return m

t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
    n = int(input())
    if isTidy(n):
        print("Case #{}: {}".format(i, n))
    else:
        print("Case #{}: {}".format(i, findLargestTidyNumberBelow(n)))

