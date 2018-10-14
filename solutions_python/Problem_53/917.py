def snap(l):
    if not l:
        return []
    if (l[0]):
        l = [l[0]] + snap(l[1:])
    l[0] = 1 - l[0]
    return l

def light_bulb(l):
    if not l:
        return 1
    else:
        if not l[0]:
            return 0
        else:
            return light_bulb(l[1:])

def solve(filename):
    #"""Solves the problem"""

    f = open(filename, 'r')
    T = int(f.readline())
    for case in range(0,T):
        [N, K] = [int(e) for e in f.readline().split()]
        snappers = N * [0]
        for i in range(0,K):
            snappers = snap(snappers)
        print("Case #" + str(case+1) + ": ", end = "")
        if (light_bulb(snappers)):
            print("ON")
        else:
            print("OFF")

solve("A-small.in")
