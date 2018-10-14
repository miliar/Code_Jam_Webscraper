#!/usr/bin/python3
import random

def solve(a, p):
    a0 = a[:]
    res = [0] * a[0]
    if p == 2:
        res += [1] * a[1]
    elif p == 3:
        while a[1] > 0 and a[2] > 0:
            res += [1, 2]
            a[1] -= 1
            a[2] -= 1
        res += ([1] * a[1]) + ([2] * a[2])
    elif p == 4:
        while a[1] > 0 and a[3] > 0:
            res += [1, 3]
            a[1] -= 1
            a[3] -= 1
        while a[2] >= 2:
            res += [2, 2]
            a[2] -= 2
        if a[2] > 0:
            res += [2]
            a[2] -= 1
        while a[1] > 0:
            res += [1]
            a[1] -= 1
        while a[3] > 0:
            res += [3]
            a[3] -= 1
    #print(a0)
    #print(res)
    for i in range(p):
        assert a0[i] == res.count(i)
    ans = 0
    cur = 0
    for x in res:
        if cur % p == 0:
            ans += 1
        cur += x    
    return ans

#---------
nt = int(input())
for t in range(nt):
    #print("Test ", t)
    n, p = map(int, input().split())
    x = list(map(int, input().split()))
    a = [0] * p
    for v in x:
        a[v % p] += 1
    ans = solve(a, p)
    print("Case #%d: %d" % (t+1, ans))

"""
def solvestupid(a, p, res):
    done = True
    for v in a:
        if v != 0:
            done = False
    if done:
        ans = 0
        cur = 0
        for x in res:
            if cur % p == 0:
                ans += 1
            cur += x    
        return ans
    else:
        ans = 0
        for i in range(p):
            if a[i] > 0:
                a[i] -= 1
                res.append(i)
                tans = solvestupid(a, p, res)
                if tans > ans:
                    ans = tans
                res.pop()
                a[i] += 1
        return ans


for i in range(10**6):
    print(i)
    p = 4 #random.randint(2, 4)
    a = []
    m = p
    if p == 2:
        m = 3
    for i in range(p):
        a.append(random.randint(0, m))
    ans1 = solve(a[:], p)
    ans2 = solvestupid(a[:], p, [])
    if ans1 != ans2:
        print(a)
        print(ans1)
        print(ans2)
        break
"""
