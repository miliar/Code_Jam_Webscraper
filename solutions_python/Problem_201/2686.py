from math import ceil, floor

#with open('problemC.txt', 'r')  as f:
#with open('C-small-1-attempt0.in', 'r')  as f:
#with open('C-small-1-attempt1.in', 'r')  as f:
with open('C-small-1-attempt2.in', 'r')  as f:
    content = f.read().splitlines()

content = list(reversed(content))
numTestCases = int(content.pop())
#text_file = open("C-small-1-attempt0.out", "w")
#text_file = open("C-small-1-attempt1.out", "w")
text_file = open("C-small-1-attempt2.out", "w")


# for each test          
for i in range(1, numTestCases+1):
    line = content.pop().split(' ')
    n, k = int(line[0]), int(line[1])
#    print("{}, {}".format(n, k))
    
    # brute force
    stalls = n * [0]
    
    while k > 0:
        chainStart = -1
        chainEnd = -2
        bestChain = (0, -1)
    
        # find largest, continuous free space
        for index, value in enumerate(stalls):
            if value == 0:
                if chainStart == -1:
                    chainStart = index
                    chainEnd = index
                else:
                    chainEnd = index
            else:
                if chainStart != -1:
                    if chainEnd - chainStart > bestChain[1] - bestChain[0]:
                        bestChain = (chainStart, chainEnd)
                    chainStart = -1
                    chainEnd = -2
                    
            if chainEnd - chainStart > bestChain[1] - bestChain[0]:
                bestChain = (chainStart, chainEnd)

        # choose stall in middle of found free space
        stallToFill = floor((bestChain[1] - bestChain[0])/2) + bestChain[0]
        stalls[stallToFill] = 1
#        print(stalls)
#        print("chainStart:{}, chainEnd:{}, stallToFill:{}, sum:{}".format(bestChain[0], bestChain[1], stallToFill, sum(stalls)))
#        print('')
#        
        k = k - 1
    
    # compute free space to left and right of stallToFill
    
    leftSpace = stallToFill - bestChain[0]
    rightSpace = bestChain[1] - stallToFill
    
    ansMax = max(leftSpace, rightSpace)
    ansMin = min(leftSpace, rightSpace)
    
    # smart method
#    while k > 0:
#        if k == 1:
#            ansMax = ceil((n-1)/2)
#            ansMin = floor((n-1)/2)
#            break
#        else:
#            n = floor((n-1)/2)
#            k = ceil((k-1)/2)
##            print("{}, {}".format(n, k))
#            
#            ansMax = ceil((n-1)/2)
#            ansMin = floor((n-1)/2)
            
#    if ansMin == -1:
#        ansMin = 0                
    
    text_file.write("Case #{}: {} {}\n".format(i, ansMax, ansMin))
#    print("Case #{}: {} {}".format(i, ansMax, ansMin))
#    print('')
    
text_file.close()