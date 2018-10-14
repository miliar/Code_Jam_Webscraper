#!/usr/bin/python

def gcd(a, b):
    a, b = min(a, b), max(a, b)
    while a > 0: # a < b
        a, b = b % a, a
    return b



# def brute(n, pd, pg):
#     gcd_d = gcd(pd, 100)
#     a, b = pd / gcd_d, 100 / gcd_d
#     gcd_g = gcd(pg, 100)
#     c, d = pg / gcd_g, 100 / gcd_g
#     for k in range(1, n / b + 1):
#         # ???



def wild(n, pd, pg):
    if pg == 100 and pd < 100:
        return False
    if pg == 0 and pd > 0:
        return False
    gcd_d = gcd(pd, 100)
    a = 100 / gcd_d
    if n < a:
        return False
    return True



if __name__ == "__main__":
    import sys
    tests = int(sys.stdin.readline())
    for t in range(tests):
        n, pd, pg = map(int, sys.stdin.readline().split())
        possible = wild(n, pd, pg)
        print "Case #%d: %s" % (t + 1, "Possible" if possible else "Broken")


