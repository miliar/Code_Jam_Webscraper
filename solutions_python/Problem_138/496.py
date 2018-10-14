__author__ = 'Pierre-Luc'


def solve(N,NBlocks,KBlocks,numCase):
    NBlocks.sort()
    KBlocks.sort()
    answer1 = solveStrategy1(N,list(NBlocks),list(KBlocks))
    answer2 = solveStrategy2(N,NBlocks,KBlocks)

    fOutput.write("Case #" + str(numCase+1) + ": ")
    fOutput.write(str(answer2) + " "+ str(answer1))

    fOutput.write("\n")

def solveStrategy1(N,NBlocks,KBlocks):
    numWins = 0

    for game in range(N):
        valN = NBlocks.pop(0)

        KPlayed = False
        for i in range(0,len(KBlocks)):
            if KBlocks[i] > valN:
                KBlocks.pop(i)
                KPlayed = True
                break
        if KPlayed == False:
            KBlocks.pop(0)
            numWins += 1

    return numWins
def solveStrategy2(N,NBlocks,KBlocks):
    return N-solveStrategy1(N,KBlocks,NBlocks)



fInput = open("4InputLarge.txt","r")
fOutput = open("4OutputLarge.txt","w")


T = int(fInput.readline())

for numCase in range(0,T):
    N = int(fInput.readline())
    NBlocks = fInput.readline().strip("\n").split(" ")
    NBlocks = [float(i) for i in NBlocks]

    KBlocks = fInput.readline().strip("\n").split(" ")
    KBlocks = [float(i) for i in KBlocks]

    solve(N,NBlocks,KBlocks,numCase)

