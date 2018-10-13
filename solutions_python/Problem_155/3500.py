T = int(raw_input())

for casos in xrange(T):
    Smax, Pessoas = raw_input().split(' ')
    Smax = int(Smax)

    tamVetor = len(Pessoas) - 1

    i = tamVetor
    contaFaltam = 0
    while(i >= 0):
        faltamTemp = Smax - sum(list(map(int, Pessoas[:i])))
        if(faltamTemp > 0):
            contaFaltam += faltamTemp
            Pessoas = str(int(Pessoas[0]) + faltamTemp) + Pessoas[1:]

        i -= 1
        Smax -= 1

    print("Case #%d: %d" %(casos+1, contaFaltam))