from copy import deepcopy
from sys import stdin


EXTRA_WEIGHT = 0.00000001


def getKenWeight(naomiChosen, kenWeights):
    options = filter(lambda w: w > naomiChosen, kenWeights)

    if len(options) == 0:
        # No larger weights, choose smallest of current weights
        options = kenWeights

    # Choose smallest of the options
    return min(options)


def chooseDeceitWeight(naomiWeights, kenWeights):
    if len(naomiWeights) == 1:
        # Only one to choose from
        choice = naomiWeights[0]
        lie = choice
    else:
        # Determine the blocks that naomi has that can not possibly
        # win against any blocks
        worstKen = min(kenWeights)
        definiteLosers = filter(lambda w: w < worstKen, naomiWeights)

        kenBest = max(kenWeights)

        # If there are no definite losers, need to choose from
        # other blocks
        if len(definiteLosers) > 0:
            # Choose the smallest weight naomi has, and lie to say it's
            # barely smaller than ken's largest weight to take out ken's
            # largest block
            choice = min(definiteLosers)

            if choice > kenBest:
                # no need to lie
                lie = choice
            else:
                lie = kenBest - EXTRA_WEIGHT  # subtract a small amount
        else:
            # All naomi's pieces can beat one of ken's pieces. Take naomi's
            # lightest block and lie to say it's larger than ken's largest
            # weight to force ken to actually select his lightest
            choice = min(naomiWeights)
            lie = kenBest + EXTRA_WEIGHT

    return choice, lie


def chooseNormalWeight(naomiWeights, kenWeights):
    if len(naomiWeights) == 1:
        # Only one to choose from
        choice = naomiWeights[0]
    else:
        # Determine the blocks that naomi has that can not possibly
        # win against any blocks
        worstKen = min(kenWeights)
        definiteLosers = filter(lambda w: w < worstKen, naomiWeights)

        if len(definiteLosers) > 0:
            # If naomi has pieces that are guaranteed to lose, choose the
            # largest one to knock out ken's first larger piece
            choice = max(definiteLosers)
        else:
            # All of naomi's pieces will beat one of ken's pieces
            # start with the smallest
            choice = min(naomiWeights)

    return choice


def handleDeceit(naomiWeights, kenWeights):
    score = 0

    # Note: no two blocks have the same weight (i.e., no ties)

    # Handle the case where there's only one block remaining
    if len(naomiWeights) == 1:
        # Scores for deceitful and non-deceitful are the same in this case
        if naomiWeights[0] > kenWeights[0]:
            score = 1  # Naomi won
        else:
            score = 0  # Ken won

        # No more weights to choose from
        naomiWeights = []
        kenWeights = []
    else:
        chosenActual, chosenLie = chooseDeceitWeight(naomiWeights, kenWeights)
        kenChoice = getKenWeight(chosenLie, kenWeights)

        realWin = (chosenActual > kenChoice)
        lieWin = (chosenLie > kenChoice)

        # Fraud alert...
        if realWin != lieWin:
            print "KEN KNOWS NAOMI IS LYING!!!!!!!!!!!!"
            exit(1)

        # Figure out naomi's score
        score = 1 if realWin else 0

        # Remove the used pieces
        naomiWeights.remove(chosenActual)
        kenWeights.remove(kenChoice)
        
    return score, (naomiWeights, kenWeights)


def handleNormal(naomiWeights, kenWeights):
    score = 0

    # Note: no two blocks have the same weight (i.e., no ties)

    # Handle the case where there's only one block remaining
    if len(naomiWeights) == 1:
        # Scores for deceitful and non-deceitful are the same in this case
        if naomiWeights[0] > kenWeights[0]:
            score = 1  # Naomi won
        else:
            score = 0  # Ken won

        # No more weights to choose from
        naomiWeights = []
        kenWeights = []
    else:
        naomiChoice = chooseNormalWeight(naomiWeights, kenWeights)
        kenChoice = getKenWeight(naomiChoice, kenWeights)

        # Figure out naomi's score
        score = 1 if (naomiChoice > kenChoice) else 0

        # Remove the used pieces
        naomiWeights.remove(naomiChoice)
        kenWeights.remove(kenChoice)
        
    return score, (naomiWeights, kenWeights)


def handleTest(case, lines):
    # Input is three lines
    #    N
    #    naomi's weights
    #    ken's weights
    #
    numBlocks = int(lines[0])  # N: number of blocks each player has
    naomiWeights = map(float, lines[1].split(" "))
    kenWeights = map(float, lines[2].split(" "))

    ##### error checking
    #
    if len(naomiWeights) != numBlocks:
        print "Error: naomi does not have", numBlocks, "weights!"
        print lines
        print naomiWeights
        exit(1)
    if len(kenWeights) != numBlocks:
        print "Error: ken does not have", numBlocks, "weights!"
        print lines
        print kenWeights
        exit(1)

    deceitTotal = 0
    regularTotal = 0

    deceitWeights = (deepcopy(naomiWeights), deepcopy(kenWeights))
    normalWeights = (deepcopy(naomiWeights), deepcopy(kenWeights))

    # Note: weights are 0.0 to 1.0 EXCLUSIVE
    # Note: naomi always goes first in each "round"
    for round in range(numBlocks):
        deceitScore, deceitWeights = handleDeceit(*deceitWeights)
        normalScore, normalWeights = handleNormal(*normalWeights)

        deceitTotal += deceitScore
        regularTotal += normalScore

    # output two digits:
    #    -- naomi's DECEITFUL score
    #    -- naomi's REGULAR score
    print "Case #%s: %s %s" % (case, deceitTotal, regularTotal)


if __name__ == '__main__':
    data = stdin.read().strip()
    lines = data.split("\n")

    numTests = int(lines[0])

    case = 1
    index = 1
    while index < len(lines):
        linesPerTest = 3

        testLines = lines[index:index + linesPerTest]
        handleTest(case, testLines)

        case += 1
        index += linesPerTest
