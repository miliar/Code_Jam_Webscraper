__author__ = 'rutger'

def isTidy(s):
    if len(s) <= 1:
        return True

    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True

def findDirtyIndex(s, idx):
    for i in range(idx - 1, 0, -1):
        if s[i] > s[idx]:
            return i
    return 0

def solve(s):
    if len(s) == 1:
        return s

    i = len(s) - 1
    while i > 0 and not isTidy(s):
        # fix digit i
        dirty = findDirtyIndex(s, i)
        for j in range(dirty + 1, len(s)):
            s[j] = 9
        s[dirty] -= 1
        i -= 1
    return s


def toString(s):
    res = ''
    for x in s:
        if x == 0:
            continue
        res += str(x)

    return res


for T in range(int(input())):
    s = list(map(int, list(input())))
    res = solve(s)
    result = toString(res)
    print("Case #%d: %s" % (T + 1, result))