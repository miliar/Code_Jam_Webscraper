import sys
sys.setrecursionlimit(5000)
T = int(input())

def split(space, people):
    #print(str(space) + " "+str(people))
    spacing = space-1
    curMin = spacing // 2
    curMax = spacing - curMin
    #print(str(curMax) + " "+str(curMin))
    if tuple([space, people]) in stalling:
        #print("HERE " + str(space) + " " +str(people))
        return stalling[tuple([space, people])]
    else:
        if people > 1:
            persons = people - 1
            #print("PERSONS " +str(persons))
            minP = persons // 2
            maxP = persons -minP
            #print("MINPERSONS " +str(minP))
            #print("MAXPERSONS " +str(maxP))
            if people % 2 == 1:
                trueMax, trueMin = split(curMin, minP)
                stalling[tuple([curMin, minP])] = [trueMax, trueMin]
            else:
                trueMax, trueMin = split(curMax, maxP)
                stalling[tuple([curMax, maxP])] = [trueMax, trueMin]
            #print(stalling)
            return [trueMax, trueMin]
        else:
            #print(curMax)
            #print(curMin)
            #print(spacing)
            stalling[tuple([space, people])] = [curMax, curMin]
            #print(stalling)
            return [curMax, curMin]
    

for x in range(T):
    stalling = {(0,0): [0,0]}
    N, K = map(int, input().split(" "))
    stalling[tuple([N, K])] = split(N, K)
    caseMax, caseMin = stalling[tuple([N, K])]
    print("Case #"+str(x+1)+": "+str(caseMax)+" "+str(caseMin))
    #print(stalling)
