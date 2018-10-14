#!/usr/bin/python

def doit():
    r, k, n = map(int, raw_input().split())
    a = map(int, raw_input().split())

    def get(x):
        y = x
        s = a[x]
        while s <= k:
            x = (x+1)%n
            s += a[x]
            if x == y: break
        return x, s-a[x]

    now = 0
    next = [-1]*n
    num = [0]*n
    while next[now] == -1:
        x, y = get(now)
        next[now] = x
        num[now] = y
        now = x

    i, pre, npre = 0, 0, 0
    while i != now:
        pre += num[i]
        i = next[i]
        npre += 1
        if npre == r: return pre

    snum = [0]
    r -= npre
    loop = 0
    while True:
        snum.append(snum[-1]+num[i])
        loop += 1
        i = next[i]
        if i == now:
            break
    return pre + r / loop * snum[-1] + snum[r % loop]

t=input()
for x in xrange(t):
    print 'Case #%d: %d' % (x+1, doit())
