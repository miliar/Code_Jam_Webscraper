#!/usr/bin/python3


fin = open('A-large-0.in', 'r')
fout = open('A-large-0.out', 'w')


def solve():
    smax, s = list(fin.readline().split())
    cur = 0
    ans = 0
    for i, x in enumerate(map(int, s)):
        if cur < i:
            ans += i - cur
            cur = i
        cur += x
    fout.write("%d\n" % ans)

T = int(fin.readline())

for i in range(1, T + 1):
    fout.write("Case #%d: " % i)
    solve()

fin.close()
fout.close()
