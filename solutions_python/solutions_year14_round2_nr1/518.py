#!/usr/bin/python3

def readln(): return tuple(map(int, input().split()))

def str2str(s):
    res = []
    cnt = []
    for c in list(s):
        if len(res) == 0 or res[-1] != c:
            res.append(c)
            cnt.append(1)
        else:
            cnt[-1] += 1
    return (res, cnt)

def solve(number):
    n, = readln()
    lst = [input().strip() for _ in range(n)]
    tmp = []
    v = str2str(lst[0])[0]
    for s in lst:
        r, c = str2str(s)
        if r != v:
            print("Case #%d: Fegla Won" % number)
            return
        tmp.append(c)
    ans = 0
    for t in zip(*tmp):
        m = sum(t) // len(t)
        ans += sum([abs(i - m) for i in t])
    print("Case #%d: %d" % (number, ans))

if __name__ == '__main__':
    t, = readln()
    for _ in range(t):
        solve(_ + 1)