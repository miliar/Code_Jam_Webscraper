from __future__ import print_function
import sys

# print to stderr for debugging
enableDebug = False
def printe(*stuff):
    if enableDebug:
        print(*stuff, file=sys.stderr) 


# Open file for processing
filename = sys.argv[1]
inputFile = open(filename, 'r')
lines = [l.rstrip('\n') for l in inputFile]
linesIter = iter(lines)
nCases = int(linesIter.next())


def tSearch(low, high, f):

    while high - low > 2:

        lowerThird = (3 * low + high - low) // 3
        upperThird = (3 * low + 2*(high - low)) // 3

        fLow = f(lowerThird)
        fHigh = f(upperThird)

        if fLow > fHigh:
            low = lowerThird
        else:
            high = upperThird


    f0 = f(low)
    f1 = f(low+1)
    f2 = f(low+2)

    if f0 <= f1 and f0 <= f2:
        return low
    elif f1 <= f0 and f1 <= f2:
        return low+1
    else:
        return low+2

# Process each case
for iCase in range(1,nCases+1):
    printe("\nProcessing case " + str(iCase))

    # Solve problem
    items = [int(x) for x in linesIter.next().split()]

    dragonHealth = items[0]
    dragonAttack = items[1]
    knightHealth = items[2]
    knightAttack = items[3]
    buffAmount = items[4]
    debuffAmount = items[5]



    # Decide how many turns to buff for
    # def turnsToKill(x): 
    #     return x + (knightHealth-1) // (dragonAttack + x*buffAmount) + 1

    # How long the TOTAL fight takes if you debuff nDebuff times
    def simulate(nDebuff, nBuff):

        # printe("--Trying debuff = {}".format(nDebuff))
        nTurns = 0
        health = dragonHealth
        kA = knightAttack
        A = dragonAttack
        kH = knightHealth

        # Debuff phase
        doubleHeal = False
        while nDebuff > 0:

            # My move
            if(health - (kA - debuffAmount) <= 0):
                health = dragonHealth # heal
                if doubleHeal: return 1E15
                doubleHeal = True
            else:
                kA = max((0, kA - debuffAmount)) # debuff
                nDebuff -= 1
                doubleHeal = False

            # His move
            health -= kA

            nTurns += 1
        
        # Kill phase
        doubleHeal = False
        while nBuff > 0:

            # My move
            if(health - kA <= 0):
                health = dragonHealth # heal
                if doubleHeal: return 1E15
                doubleHeal = True
            else:
                A += buffAmount
                nBuff -= 1
                doubleHeal = False

            # His move
            health -= kA

            nTurns += 1

        # Kill phase
        doubleHeal = False
        while kH > 0:

            # My move
            if(health - kA <= 0 and kH - A > 0):
                health = dragonHealth # heal
                if doubleHeal: return 1E15
                doubleHeal = True
            else:
                kH -= A
                doubleHeal = False

            # His move
            health -= kA

            nTurns += 1

        # printe("  -->   nTurns = {}".format(nTurns))
        return nTurns


    best = 1E15
    for nBuff in range(0,105):
        for nDebuff in range(0,105):
            best = min((best, simulate(nDebuff, nBuff)))

    if best == 1E15:
        print("Case #{}: {}".format(iCase, "IMPOSSIBLE"))
    else:
        print("Case #{}: {}".format(iCase, best))
