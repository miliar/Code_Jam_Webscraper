import sys, os

puzzles = list()

FILENAME = 'D-large.in'

def solveOptimal(puzzle):
    naomi, ken = puzzle
    naomi = sorted(naomi)
    ken = sorted(ken)
    naomiScore = 0
    while len(naomi) > 0:
        chosenNaomi = naomi.pop(0)
        chosenKen = 0.
        for block in ken:
            if block > chosenNaomi:
                chosenKen = block
                break
        if chosenKen == 0.:
            chosenKen = ken.pop(0)
            naomiScore += 1
        else:
            ken.remove(chosenKen)
    return naomiScore

def solveDeceitful(puzzle):
    naomi, ken = puzzle
    naomi = sorted(naomi)
    ken = sorted(ken)
    naomiScore = 0

    while len(naomi) > 0:
        if ken[-1] > naomi[-1]: #Naomi needs to sacrifice her lighter stone for Ken to use his larger one
            chosenNaomi = naomi.pop(0)
            if ken[-1] > chosenNaomi: #Naomi says her lighter stone is one gram lower than the heavier Ken has
                chosenKen = ken.pop()
            else: #Naomi stones are all heavier than Ken's
                ken.pop(0) #he s playing his worst stone, but we know it s already over
                naomiScore += 1
        else:
            #it's over. Naomi's stones are heavier one for one of Ken's
            #Therefore, by being deceitful, she can say her lighter stone is 1g heavier than the heavier block of Ken
            #and Ken will just use his lighter block to minimize the damage
            naomi.pop()
            ken.pop()
            naomiScore += 1
    return naomiScore


with open(FILENAME, 'r') as f:
    nbTestCases = int(f.readline())
    for _ in range(nbTestCases):
        f.readline()
        puzzles.append([[float(n) for n in f.readline().strip().split()], [float(n) for n in f.readline().strip().split()]])

printResult = ''
for (i, puzzle) in enumerate(puzzles):
    print puzzle
    #print 'Case #%s: %s\n' % (i+1, solve(puzzle))
    printResult += 'Case #%s: %s %s\n' % (i+1, solveDeceitful(puzzle), solveOptimal(puzzle))

print printResult
#sys.exit(0)

if os.path.isfile('result'):
    os.remove('result')
with open('result', 'w') as f:
    f.write(printResult[:-1])