


def solveFlip(s, k, n, prev):
    if checkFlipped(s):
        return n
    index = findMostUnflipped(s, k)


    if index + k > len(s) - 1:
        index = len(s) - k

    if prev == index:
        return "IMPOSSIBLE"
    else:
        prev = index

    for i in xrange(k):
        s[index] = (s[index] + 1) % 2
        index += 1
    return solveFlip(s, k, n + 1, prev)

def checkFlipped(s):
    for i in s:
        if i == 0:
            return False
    return True

def findMostUnflipped(s, k):
    for i in xrange(k, 0, -1):
        n = 0
        for j in xrange(len(s)):
            if s[j] == 0:
                n += 1
            else:
                n = 0

            if n == i:
                return j - n + 1
    return None

def buildArray(s):
    x = []
    for i in xrange(len(s)):
        if s[i] == '+':
            x.append(1)
        else:
            x.append(0)
    return x

t = int(raw_input())
for i in xrange(1, t + 1):
    n = raw_input().split(" ")
    s = n[0]
    k = int(n[1])
    s = buildArray(s)
    x = solveFlip(s, k, 0, -1)
    print "Case #{}: {}".format(i, x)

