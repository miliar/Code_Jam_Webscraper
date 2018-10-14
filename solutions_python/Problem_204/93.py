import sys
import math
stdin = sys.stdin
ncases = int(stdin.readline())

for ncase in range(ncases):
    N, P = map(int, stdin.readline().strip().split(' '))
    ingr = list(map(int, stdin.readline().strip().split(' ')))
    ingrSizes = []
    for line in range(N):
        ingrSizes.append(list(sorted(map(int, stdin.readline().strip().split(' ')))))
 
    # print(ingrSizes)
    numFound = 0
    cntr = 1
    while True:

        if any(len(v) == 0 for v in ingrSizes): break

        minVals = [0.8 * v[0] / ingr[i] for i, v in enumerate(ingrSizes) if len(v) > 0]
        cntr = max(cntr, int(min(minVals)))
        
        # print("trying {0}".format(cntr))
        skip = False
        while not skip:
            skip = False
            for i, sizes in enumerate(ingrSizes):
                targetSize = cntr * ingr[i]
                minSize = math.ceil(targetSize * 0.9)
                maxSize = math.floor(targetSize * 1.1)
                found = False
                skipCount = 0
                for c, s in enumerate(sizes):
                    if s < minSize: skipCount += 1; continue
                    if s <= maxSize:
                        found = True
                    break
                ingrSizes[i] = ingrSizes[i][skipCount:]
                if not found:
                    skip = True
                    break
            
            if not skip:
                numFound += 1
                for i in range(len(ingrSizes)):
                    # print("adding {0} x {1}".format(cntr, ingrSizes[i][0]))
                    ingrSizes[i] = ingrSizes[i][1:]
        
        cntr += 1

    # print(ingr)
    # print(ingrSizes)
    result = numFound
    print('Case #{0}: {1}'.format(ncase + 1, result))