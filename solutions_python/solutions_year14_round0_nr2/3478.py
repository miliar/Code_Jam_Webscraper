#!/usr/bin/python
import sys

def timeForIteration(X, F0, N, F, C):
    """ X is the goal
        F0 is the initial cookie earn rate
        N is the number of farms to buy
        F is the farm production rate
        C is the farm cost
        """
    firstFactor = X / (F0+N*F)

    secondFactor = 0
    if N > 0:
        for z in range(0,N):
            secondFactor = secondFactor + ( C / (F0 + z*F))

    return firstFactor + secondFactor

fileName = sys.argv[1]

f = open(fileName, "r")
a = open(fileName + "-answer", "w")

lines = f.read().split("\n")
cases = int(lines.pop(0))

cookieProductionRate = 2

for case in range(1,cases+1):
    params = map(float, lines.pop(0).split(" "))
    C_farmCost           = params[0]
    F_farmProductionRate = params[1]
    X_goal               = params[2]
    print("{} {} {}".format(C_farmCost, F_farmProductionRate, X_goal));

    lastT = 2000000000000000000
    solved = False
    N = 0
    while solved == False:
        t = timeForIteration(X_goal, cookieProductionRate, N, F_farmProductionRate, C_farmCost)
#       print("?  {} {:.7f}".format(N, t))
        if t < lastT:
            lastT = t
        else:
            solved = True
            break
        N = N + 1

    if solved == True:
        print("-> {} {:.7f}".format(N, lastT))
    else:
        print("!! {} {:.7f}".format(N, t))

    a.write("Case #{}: {:.7f}\n".format(case, lastT))


