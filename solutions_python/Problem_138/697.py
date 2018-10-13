def solveC(file):
    data = ''
    resultTotal = []
    with open(file) as f:
        T = f.readline()
        T = int(T.strip())
        for index in xrange(T):
            N = int(f.readline().strip())
            BlocksNDeceit = [float(val.strip()) for val in f.readline().strip().split(' ')]
            BlocksKDeceit = [float(val.strip()) for val in f.readline().strip().split(' ')]

            BlocksNDeceit.sort(reverse = True)
            BlocksNReal = [val for val in BlocksNDeceit]

            BlocksKDeceit.sort(reverse = True)
            BlocksKReal = [val for val in BlocksKDeceit]

            pointsNDeceit = 0
            pointsNReal = 0
            for i in xrange(len(BlocksNDeceit)):
                #Real war
                if BlocksNReal[0] > BlocksKReal[0]:
                    #Ken can't win, removes one of his lesser value blocks
                    BlocksKReal = BlocksKReal[:-1]
                    pointsNReal += 1
                    BlocksNReal = BlocksNReal[1:]
                else:
                    BlocksKReal = BlocksKReal[1:]
                    BlocksNReal = BlocksNReal[1:]
                
                #Deceitful war
                if BlocksKDeceit[0] > BlocksNDeceit[0]:
                    #Naomi can't win, uses one of her lesser value blocks and tricks ken
                    BlocksKDeceit = BlocksKDeceit[1:]
                    BlocksNDeceit = BlocksNDeceit[:-1]
                else:
                    #Naomi is going to win, but don't want to remove her best block, chooses a lesser one
                    
                    for val in range(len(BlocksNDeceit))[::-1]:
                        if BlocksNDeceit[val] > BlocksKDeceit[-1]:
                            NChoose = val
                            break
                    
                    if len(BlocksNDeceit) > 1:
                        BlocksTemp = BlocksNDeceit[0:NChoose] + BlocksNDeceit[NChoose + 1:]
                        BlocksNDeceit = BlocksTemp
                    pointsNDeceit += 1
                    BlocksKDeceit = BlocksKDeceit[:-1]
                    
            
            resultTotal.append([pointsNDeceit,pointsNReal])
    

        with open('resultC.txt','w') as r:
            for index in xrange(len(resultTotal)):
                r.write('Case #{0}: {1} {2} \n'.format(index + 1, resultTotal[index][0], resultTotal[index][1]))
