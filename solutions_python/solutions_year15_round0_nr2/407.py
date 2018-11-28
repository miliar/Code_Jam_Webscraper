#!/usr/bin/env python


def read():
    input()
    return map(int, raw_input().split())


def calc(vList, limit):
    cnt = 0
    for i in range(len(vList)):
        cnt += (vList[i] - 1) / limit
    return cnt + limit


def work(cases, vList):
    ans = 1 << 30
    
    for limit in range(1, 1001):
        ans = min(ans, calc(vList, limit))
    
    print "Case #%d: %d" % (cases, ans)


if __name__ == "__main__":
    for i in range(int(raw_input())):
        work(i + 1, read())
