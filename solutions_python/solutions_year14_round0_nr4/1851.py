nCases = eval(input())

for caseNum in range(nCases):

    input()

    naomi = list(map(float, input().split()))
    ken   = list(map(float, input().split()))

    naomi.sort()
    ken.sort()

    
    dWar = 0
    dNaomi = list(naomi)
    dKen = list(ken)

    for i in range(len(naomi)):
        if dNaomi[-1] > dKen[-1]:
            dNaomi.pop()
            dWar += 1
        else:
            dNaomi.pop(0)
        dKen.pop()

    war = 0
    wNaomi = list(naomi)
    wKen = list(ken)

    for i in range(len(naomi)):
        if wNaomi[-1] > wKen[-1]:
            wKen.pop(0)
            war += 1
        else:
            kenBlock = min(x for x in wKen if x > wNaomi[-1])
            wKen.remove(kenBlock)
        wNaomi.pop()
        
    print('Case #{}: {} {}'.format(caseNum + 1, dWar, war))
