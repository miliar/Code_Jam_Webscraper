__author__ = 'rutger'

def transformToBoolean(s):
    b = []
    for c in s:
        b.append(c == '+')
    return b

def isSolved(b):
    return sum(b) == len(b)

def stripLeft(b):
    idx = 0
    for i in range(len(b)):
        if not b[i]:
            idx = i
            break

    return b[idx:]

def flip(b, k):
    for i in range(k):
        b[i] = not b[i]
    return b

def solve(s, k):
    b = transformToBoolean(s)
    if isSolved(b):
        return 0

    counter = 0
    while not isSolved(b):
        b = stripLeft(b)
        currentLen = len(b)

        if currentLen < k:
            return -1
        b = flip(b, k)
        counter += 1
    return counter

for T in range(int(input())):
    s, k = input().split(' ')
    k = int(k)
    res = solve(s, k)
    if res == -1:
        pass
        print('Case #%d: %s' % (T + 1, 'IMPOSSIBLE'))
    else:
        print('Case #%d: %s' % (T + 1, str(res)))