#!/usr/bin/pypy

def calc(l):
    ls = sorted(l)
    res = 0
    for x in ls:
        res += l.index(x)
        l.remove(x)
    return res

def solve1(l):
    A = l[:]
    am = max(A)
    ind = A.index(am)
    A.remove(am)
    return min([calc(A[:i])+calc(list(reversed(A[i:])))+abs(i-ind) for i in range(len(A)+1)])

def solve3(l):
    A = l[:]
    res = 0
    for x in sorted(A):
        ind = A.index(x)
        res += min(ind,len(A)-1-ind)
        A.remove(x)
    return res

def solve():
    N = int(raw_input())
    A = map(int,raw_input().split())
    res3 = solve3(A)
    #res2 = solve2(A)
    #if res3 != res2:
    #    print 'Bad', A, res3, res2
    return res3

def solve2(l,lvl=0):
    u = [tuple(l)]
    au = set([tuple(l)])
    cnt = 0
    while 1:
        u2 = []
        for a in u:
            a = list(a)
            for i in range(len(a)-1):
                if a[i]>a[i+1]:
                    first = i
                    break
            else:
                return cnt
            for i in range(len(a)-2,0,-1):
                if a[i]<a[i+1]:
                    last = i
                    break
            else:
                return cnt
            if first > last:
                return cnt
            for i in range(len(a)-1):
                a[i], a[i+1] = a[i+1], a[i]
                t = tuple(a)
                if t not in au:
                    u2.append(t)
                    au.add(t)
                a[i], a[i+1] = a[i+1], a[i]

        cnt += 1
        u = u2

if __name__ == "__main__":
    T = int(raw_input())
    for t in range(1,T+1):
        print "Case #%d:"%t,solve()
