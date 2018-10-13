f = open('C-small-1-attempt0.in', 'r')
g = open('output_C_small.txt', 'w')
num_loops = int(f.readline())

for testCase in range(0,num_loops):
    inputs = str(f.readline()).split()
    inputs = [int(inputs[0]),int(inputs[1])]
    
    # N people, K stalls
    N = inputs[0]
    K = inputs[1]

    stallGroups = []
    stallGroups.append(N)

    for i in range(0,K):
        maxStalls = max(stallGroups)
        bestGroupIndex = min([i for i, j in enumerate(stallGroups) if j == maxStalls])
        bestmax = (maxStalls - 1)//2
        bestmin = (maxStalls)//2

        #print(stallGroups)
        #update stalls after insertion
        # if odd
        if (maxStalls %2 ==0):
            stallGroups[bestGroupIndex] = int((maxStalls - 2) / 2)
            stallGroups.insert(bestGroupIndex+1,int(maxStalls/2))
        else:
            stallGroups[bestGroupIndex] = int((maxStalls - 1) / 2)
            stallGroups.insert(bestGroupIndex+1,int((maxStalls - 1) / 2))
    

    string = str('Case #' + str(testCase+1) + ': ' + str(bestmin)+ ' ' + str(bestmax) + '\n')
    g.write(string)
f.close()
g.close()
