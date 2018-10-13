import math

f = open("A-small-attempt4.in","r")
g = open("A-small4.out","w")

cases = int(f.readline())

i = 0

print cases

while i < cases:

    params = f.readline().rstrip().split(" ")

    A = int(params[0])
    otherMotes = int(params[1])

    listMotes = f.readline().rstrip().split(" ")

    listMotes = map(int,listMotes)

    listMotes.sort()

    opsCount = 0

    for m in range(0,otherMotes):

        breakout = 0
        
        if A > listMotes[m]:
            A += listMotes[m]

        elif A <= listMotes[m]:

            tempOpsCount = 0

            copyA = A

            copyA += copyA - 1

            tempOpsCount += 1

            while copyA <= listMotes[m]:
                copyA += copyA - 1
                tempOpsCount += 1

                if tempOpsCount >= otherMotes - (m):
                    opsCount += otherMotes - (m)
                    breakout = 1
                    break

            if breakout == 1:
                break
            
            else:
                opsCount += tempOpsCount
                A = copyA
                A += listMotes[m]
                
    i += 1
    
    g.write("Case #" + str(i) + ": " + str(opsCount)+"\n")


print i
