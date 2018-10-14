#!/usr/bin/python
import sys

def war(naomi, ken):
    points = 0
    for n in naomi:
        for k in ken:
            if k > n:
                ken.remove(k)
                break
        else:
            points += 1
            del ken[0]
    return points

def dwar(naomi, ken):
    #print "dwar", naomi, ken
    points = 0
    for i,n in enumerate(naomi):
        if all(x > y for x,y in zip(naomi[i:], ken)):
            points += len(ken)
            break
        if n > ken[-1]:
            points += len(ken)
            break
        else:
            del ken[-1]
    return points

def solve(naomi, ken):
    naomi.sort()
    ken.sort()
    return (dwar(naomi[:], ken[:]), war(naomi[:], ken[:]))

def parse_case(*args):
    N = R(int)
    naomi = map(float, R().split()[:N])
    ken = map(float, R().split()[:N])
    return (naomi, ken)

def format_ret(naomi, ken):
    return "%d %d" % (naomi, ken)

def R(cast = None):
    ret = sys.stdin.readline().strip()
    if cast is not None:
        ret = cast(ret)
    return ret

def W(msg, *args):
    sys.stdout.write((msg + "\n") % args)

def main():
    cases = R(int)
    for i in range(1,cases+1):
        ret = solve(*parse_case())
        W("Case #%d: %s", i, format_ret(*ret))

if __name__ == '__main__':
    main()
