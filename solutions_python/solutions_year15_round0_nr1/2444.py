import sys

def debug(x):
#    print(x)
    return

def solve(t):
    data = input().split()
    sMax = int(data[0])
    sList = [int(c) for c in data[1]]
    #debug("sMax: " + str(sMax))
    #debug("sList: " + str(sList))
    standedAudiences = 0
    invitingAudiences = 0
    for i in range(len(sList)):
        #debug("sList[" + str(i) + "]: " + str(sList[i]))
        if sList[i] == 0:
            continue

        if standedAudiences < i:
            requiredAudiences = i - standedAudiences
            invitingAudiences += requiredAudiences
            standedAudiences += requiredAudiences

        standedAudiences += sList[i]

    print("Case #" + str(t + 1) + ": " + str(invitingAudiences))

T = int(input())

for t in range(T):
    solve(t)