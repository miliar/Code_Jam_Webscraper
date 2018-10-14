def requiredRounds(pancakes):
    maxPancakes = max(pancakes)
    if maxPancakes <= 3:
        return maxPancakes

    minAdditionalRounds = maxPancakes
    for k in range(1, maxPancakes/2+1):
        newPancakes = [pancake for pancake in pancakes if not pancake == maxPancakes]
        additionalRounds = len(pancakes) - len(newPancakes)
        if additionalRounds > minAdditionalRounds:
            continue
        newPancakes += (len(pancakes)-len(newPancakes))*[maxPancakes - k, k]
        additionalRounds += requiredRounds(newPancakes)
        if additionalRounds < minAdditionalRounds:
            minAdditionalRounds = additionalRounds
    return minAdditionalRounds

for case in range(int(raw_input())):
    d = int(raw_input())
    pancakes = [int(nr) for nr in raw_input().split(' ')]
    assert(len(pancakes) == d)

    nrRounds = requiredRounds(pancakes)
    print 'Case #%d: %s' % (case + 1, nrRounds)

