#!/usr/bin/env python


def read():
    return map(int, raw_input().split()[1])


def work(cases, cntList):
    ans = 0

    total = 0
    for shyness, cnt in enumerate(cntList):
        if cnt > 0 and total < shyness:
            toAdd = shyness - total
            ans += toAdd
            total += toAdd
        total += cnt
    
    print "Case #%d: %d" % (cases, ans)


if __name__ == "__main__":
    for i in range(int(raw_input())):
        work(i + 1, read())
