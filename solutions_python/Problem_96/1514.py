#!/usr/bin/env python


def gt(a, p):
    return (a / 3 + 1 if a % 3 != 0 else a / 3) >= p

def gts(a, p):
    b, c = (a / 3 + 1 if a % 3 != 0 else a / 3), (a / 3 + 1 if a % 3 == 2 else a / 3)
    if p > b + 1:
        return False
    if b != c:
        return False
    if b == 10 or b == 0:
        return False
    return True

if __name__ == "__main__":
    test_cases = int(raw_input())
    for test_case in range(1, test_cases + 1):
        data = map(int, raw_input().split())
        s, p = data[1:3]
        t = data[3:]
        res = 0
        for a in t:
            if gt(a, p):
                res += 1
            elif s > 0 and gts(a, p):
                s -= 1
                res += 1
        print "Case #%d: %d" % (test_case, res)
