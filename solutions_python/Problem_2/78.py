import sys

def mins(time):
    (h, m) = map(int, time.split(':'))
    return h*60+m  

def readtable(NX, EL, ER, turn):
    for i in range(0, NX):
        (dep, arr) = map(mins, sys.stdin.readline().split(' '))
        EL.append((dep, -1))
        ER.append((arr+turn, 1))
        
def comp(a, b):
    if(a[0] == b[0]):
        return b[1] - a[1]
    return a[0] - b[0]

def solve(EX):        
    EX.sort(comp)
    diff = 0
    min = 0
    for e in EX:
        diff += e[1]
        if diff < min:
            min = diff
    return -min

for case in range(1, int(sys.stdin.readline())+1):
    turn = int(sys.stdin.readline())
    (NA, NB) = map(int, sys.stdin.readline().split(' '))
    EA = []
    EB = []
    readtable(NA, EA, EB, turn)
    readtable(NB, EB, EA, turn)
    print "Case #%d: %d %d" % (case, solve(EA), solve(EB))
            