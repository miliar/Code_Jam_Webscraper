def xor(li):
    if len(li) == 0:
        return None
    return reduce(lambda x, y: x ^ y, li)

def rec(li, idx, li1, li2, max):
    #print locals()
    if idx == len(li):
        return max
    x1 = xor(li1)
    x2 = xor(li2)
    if x1 != None and x2 != None and x1 == x2:
        return sum(li1)
    l1 = li1[:]
    x = li[idx]
    l1.remove(x)
    l2 = li2[:]
    l2.append(x)
    rval = rec(li, idx + 1, l1, l2, max)
    if rval > max:
        max = rval
    rval = rec(li, idx + 1, li1, li2, max)
    if rval > max:
        max = rval
    return max

def solve(li):
    li.sort()
    max = 0
    max = rec(li, 0, li[:], [], max)
    if max > 0:
        return max
    return "NO"

import sys
sys.setrecursionlimit(10000)


t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    li = map(int, raw_input().split())
    r = solve(li)
    print "Case #{0}: {1}".format(i + 1, r)
