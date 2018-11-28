nCases = eval(input())

for caseNum in range(nCases):

    [c, f, x] = map(float, input().split())

    speed = 2
    patienceForBuilding = 0
    noBuyETA = x / speed

    while True:
        patienceForBuilding += c / speed
        speed += f
        buyETA = patienceForBuilding + x / speed

        if (noBuyETA < buyETA):
            break
        noBuyETA = buyETA

    print('Case #{}: {}'.format(caseNum + 1, noBuyETA))
