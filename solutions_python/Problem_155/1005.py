import sys


def printer(thigns):
    for i in thigns:
        sys.stdout.write(str(i))
    print("")

t = int(sys.stdin.readline())

sys.setrecursionlimit(100000)

for j in range(t):
    linesplit = sys.stdin.readline().split()
    smax = int(linesplit[0])
    totalStanding = 0
    totalNeeded = 0
    for k in range(smax+1):
        thisOne = int(linesplit[1][k])
        if totalStanding < k:
            totalStanding += 1
            totalNeeded += 1
        totalStanding += thisOne
    printer(["Case #", j+ 1, ": ", totalNeeded])
    
