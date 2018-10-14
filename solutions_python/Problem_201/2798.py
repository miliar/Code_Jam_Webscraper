def getLR(s, i):
    l, r = 0, 0
    c = i-1
    while c>=0 and s[c] == 0:
        l+=1
        c-=1
    c = i+1
    while c<len(s) and s[c] == 0:
        r+=1
        c+=1
    return l,r

def insert(s):
    ins = 1000000
    l, r = -1, -1
    for i in range(len(s)):
        if s[i] == 1:
            continue
        tl, tr = getLR(s, i)
        if min(tl, tr) == min(l, r) and max(tl, tr) > max(l, r):
            ins = i
            l, r = tl, tr
            continue

        if min(tl, tr) > min(l, r):
            ins = i
            l, r = tl, tr
    s.pop(ins)
    s.insert(ins, 1)
    return l, r


def algo():
    n, k = map(int, input().split())
    stall = [0] * n
    l, r = 0,0
    for i in range(k):
        l, r = insert(stall)
    return l, r


n= int(input())

for x in range(1, n+1):
    y, z = algo()
    print("Case #{}: {} {}".format(x, max(z, y), min(z, y)))
