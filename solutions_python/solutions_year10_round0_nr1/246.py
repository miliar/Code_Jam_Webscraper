import sys

def getnum():
    return [int(x) for x in sys.stdin.readline().split()]

def sol1(N, K):
    # naive solution
    x = [0 for x in range(N)]
#    print x

    i = 0
    while i < K:
        # change them until we can
        for j in range(N):
            if j == 0:
                x[j] = 1 - x[j]
            else:
                if x[j-1] == 0: # it used to be 1, so this one used to have power
                    x[j] = 1 - x[j]
                else: # the power was cut here
                    break
        i += 1

    for i in range(N):
        if x[i] != 1:
            return False

    return True

def sol2(N, K):
    cycle = 2**N-1
    if K < cycle:
        return False
    elif K == cycle:
        return True
    else:
        if K % (cycle + 1) == cycle :
            return True
        else:
            return False

N = getnum()[0]

def x():
    for i in range(1, 100000):
        for j in range(1, 100000):
            x = sol1(i, j)
            y = sol2(i, j)

            if x != y:
                print i, j, x, y
                quit()

for case in range(1, N + 1):
    sol = "ON"
    N, K = getnum()
#    print N, K
    if sol1(N, K):
        print "Case #%d: ON" % (case)
    else:
        print "Case #%d: OFF" % (case)
