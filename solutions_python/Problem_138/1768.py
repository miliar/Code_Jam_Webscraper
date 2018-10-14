def parse_file(fnIn):
    assert fnIn.endswith('.in')
    fnOut = fnIn.replace('.in', '.out')

    with open(fnOut, 'w') as fOut:
        with open(fnIn, 'rU') as fIn:
            T = int(fIn.readline())

            for n in xrange(T):
                # discard line
                fIn.readline()

                naomiWeights = map(float, fIn.readline().split())
                kenWeights = map(float, fIn.readline().split())

                deceitfulScore = play_deceitful_war(naomiWeights[:],
                        kenWeights[:])
                honestScore = play_war(naomiWeights, kenWeights)

                fOut.write('Case #%d: %d %d\n'%(n + 1, deceitfulScore,
                        honestScore))


def optimal_war_choice(weights, told):
    # Optimal Strategy:
    #   if winning is possible, win with the lowest weight possible
    #   if winning is impossible, play the lowest weight

    heavierWeights = filter(lambda wt: wt > told, weights)

    if heavierWeights:
        return min(heavierWeights)

    return min(weights)


def optimal_blind_war_choice(weights):
    return max(weights)


def optimal_deceitful_choice(naomiWeights, kenWeights):
    eps = 1e-6
    kenMaxWeight = max(kenWeights)

    # Take the lowest weight which is higher than one of Ken's weights
    choice = 0
    lowerWeights = []

    while not lowerWeights:
        possibilities = sorted(filter(lambda wt: wt > choice, naomiWeights))

        if not possibilities:
            return min(naomiWeights), kenMaxWeight - eps

        choice = possibilities[0]
        lowerWeights = sorted(filter(lambda wt: wt < choice, kenWeights))

    tell = lowerWeights[-1] - eps

    return choice, tell


def play_deceitful_war(naomiWeights, kenWeights):
    score = 0

    while naomiWeights:
        naomiChoice, tell = optimal_deceitful_choice(naomiWeights, kenWeights)
        kenChoice = optimal_war_choice(kenWeights, tell)

        score += naomiChoice > kenChoice

        naomiWeights.remove(naomiChoice)
        kenWeights.remove(kenChoice)

    return score


def play_war(naomiWeights, kenWeights):
    score = 0

    while naomiWeights:
        naomiChoice = optimal_blind_war_choice(naomiWeights)
        kenChoice = optimal_war_choice(kenWeights, naomiChoice)

        score += naomiChoice > kenChoice

        naomiWeights.remove(naomiChoice)
        kenWeights.remove(kenChoice)

    return score
