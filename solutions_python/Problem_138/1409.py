import random

inputFile = open("D-small-attempt1.in", 'r')

count =  int(inputFile.readline())

for y in range(1, count+1):
    numberOfTurns = int(inputFile.readline())
    naomiWeights = [float(f) for f in inputFile.readline().split()]
    naomiWeights.sort()
    naomiWeightsTrue = naomiWeights[:]
    kenWeights = [float(f) for f in inputFile.readline().split()]
    kenWeights.sort()
    kenWeightsTrue = kenWeights[:]

    deceitfulScore = 0
    for x in range(0, numberOfTurns):
        if naomiWeights[-1] > kenWeights[-1]:
            chosenNaomi = naomiWeights[-1]
        else:
            chosenNaomi = naomiWeights[0]

        while True:
            toldNaomi = random.random()
            if len(kenWeights) > 1:
                if kenWeights[-2] < toldNaomi < kenWeights[-1]:
                    break
            else:
                if toldNaomi < kenWeights[0]:
                    break


        possibleOptionsKen = filter(lambda n: n > toldNaomi, kenWeights)
        if len(possibleOptionsKen) > 0:
            chosenKen = possibleOptionsKen[0]
        else:
            chosenKen = kenWeights[0]
        if chosenNaomi > chosenKen:
            deceitfulScore += 1
        naomiWeights.remove(chosenNaomi)
        kenWeights.remove(chosenKen)

    warScore = 0
    for x in range(0, numberOfTurns):
        chosenNaomi = random.choice(naomiWeightsTrue)
        possibleOptionsKen = filter(lambda n: n > chosenNaomi, kenWeightsTrue)
        if len(possibleOptionsKen) > 0:
            chosenKen = possibleOptionsKen[0]
        else:
            chosenKen = kenWeightsTrue[0]
        if chosenNaomi > chosenKen:
            warScore += 1
        naomiWeightsTrue.remove(chosenNaomi)
        kenWeightsTrue.remove(chosenKen)

    print "Case #%s:" % y, deceitfulScore, warScore