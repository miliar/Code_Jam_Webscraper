f = open("data.txt", 'r')
g = open("data1.txt", 'w')
T = int(f.readline())
for i in range(1, T+1):
    N = int(f.readline())
    naomi = [float(x) for x in f.readline().split()]
    ken = [float(x) for x in f.readline().split()]
    naomi.sort()
    ken.sort()

    #Deceit war game
    iterNaomi, iterKen = 0, 0
    deceitScore = 0
    while iterNaomi <= N-1:
        if naomi[iterNaomi] > ken[iterKen]:
            deceitScore += 1
            iterKen += 1
        iterNaomi += 1

    #War game
    iterNaomi, iterKen = 0, 0
    while iterNaomi <= N-1 and iterKen <= N-1:
        while(ken[iterKen] < naomi[iterNaomi]):
            iterKen += 1
            if iterKen > N-1:
                break
        if iterKen <= N-1:
            iterNaomi += 1
            iterKen += 1
    warScore = N - iterNaomi
    g.write("Case #%d: %d %d\n" % (i, deceitScore, warScore))

f.close()
g.close()