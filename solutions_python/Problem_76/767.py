##
# CODEJAM
# prillan91
##
import sys


def solveSingle(f):
    #TEST
    N = int(f.readline())
    ints = f.readline().rstrip().split(' ')
    ints = [int(i) for i in ints]
    
    total = 0

    for i in ints:
        total = total ^ (int(i))

    if not total == 0:
        return "NO"

    ints.sort()
    #print ints
    for i in ints[1:]:
        total += i

    return total

def solve():
    f = open(sys.argv[1])
    o = open(sys.argv[1] + ".out", 'w')
    T = int(f.readline())

    for t in range(T):
        #print t + 1
        o.write("Case #" + str(t + 1) + ": " + str(solveSingle(f)) + "\n")
        


solve()
