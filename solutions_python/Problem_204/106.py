import math
def solve(casenum, N , P):
    ratio = map(int, infile.readline().split(' '))
    have = []
    for i in range(N):
        have.append(sorted(map(int,infile.readline().split(' '))))
    multiples = []
    for i in range(N):
        multiples.append([])
        for j in range(P):
            options = []
            topamt = (have[i][j] /0.9)
            botamt = (have[i][j] /1.1) 
            #print botamt, topamt
            for k in range(int(math.floor(botamt/ratio[i])), int(math.ceil(topamt/ratio[i]))+1):
                #print k
                if k*ratio[i] >= botamt and k*ratio[i]<=topamt:
                    options.append(k)
            multiples[-1].append(options)

    assert len(multiples) == N
    for i in range(N):
        assert len(multiples[i])==P
    
    #print multiples

    total = 0
    for options in multiples[0]:
        for option in options:
            goodForAll = True
            takeFrom = []
            for i in range(1, N):
                found = False
                for j in range(len(multiples[i])):
                    #print i, j
                    if option in multiples[i][j]:
                        found = True
                        takeFrom.append(j)
                        break
                if found:
                    continue
                else:
                    goodForAll = False
            if goodForAll:
                #print takeFrom
                total+=1
                for i in range(1, N):
                    #print options
                    #print takeFrom
                    multiples[i].pop(takeFrom[i-1])
                break

    print "Case #%d: %d"%(casenum, total)


infile = open('input.in', 'r')
T = int(infile.readline())
for t in range(1,T+1):
    N, P = map(int, infile.readline().split(' '))
    solve(t, N, P)
