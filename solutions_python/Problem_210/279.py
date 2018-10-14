#!/usr/bin/env python

def case(T):
    AC, AJ = map(int, input().split())
    actiC = sorted([list(map(int,input().split())) for i in range(AC)])
    actiJ = sorted([list(map(int,input().split())) for i in range(AJ)])
    if len(actiC) == 2 and check1(actiC):
        return 4
    if len(actiJ) == 2 and check1(actiJ):
        return 4
    return 2

    iaC = sum([x[1]-x[0] for x in actiC])
    iaJ = sum([x[1]-x[0] for x in actiJ])
    print(iaC, iaJ)
    print(actiC, actiJ)
    print(sorted(actiC + actiJ))
    return T

def check1(l):
    return (l[1][1] - l[0][0] > 720 and 1440 - (l[1][0] - l[0][1]) > 720)


if __name__=="__main__":
    for i in range(int(input())):
        print("Case #{}: {}".format(i+1, case(i)))
