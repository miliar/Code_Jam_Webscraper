from collections import Counter
import math
import fnmatch


T = int(raw_input().strip())
for i in range(T):
    doPrint = False
    temp = map(int, raw_input().strip().split(" "))
    N = temp[0] # total pancakes
    K = temp[1] # pancakes ordered
    pancakes = []
    for j in range(N):
        temp = map(int, raw_input().strip().split(" "))
        pancakes.append(temp)
    if doPrint: print "N, K, pancakes = ", N, K, pancakes
    
    for j in range(N):
        pancakes[j].append(2*math.pi*pancakes[j][0]*pancakes[j][1])
        pancakes[j].append(math.pi*pancakes[j][0]*pancakes[j][0])
    if doPrint: print "pancakes = ", pancakes
    
    pancakes = sorted(pancakes, key = lambda x: x[2], reverse = True)
    if doPrint: print "pancakes = ", pancakes
    
    
    firstKeep = pancakes[:K]
    tempFirstKeep = sorted(firstKeep, key = lambda x: x[3], reverse = True)
    biggestTopAreaSoFar = tempFirstKeep[0][3]
    answer = 0
    for j in range(K):
        answer += firstKeep[j][2]
    answer += biggestTopAreaSoFar
    
    if K < N:

        for j in range(K, N):
            pancakes[j].append(pancakes[j][2] + pancakes[j][3] - biggestTopAreaSoFar)
    
        replaceValues = pancakes[K:]
        replaceValues = sorted(replaceValues, key = lambda x: x[4], reverse = True)
        if doPrint: print "replaceValues = ", replaceValues
        biggestReplaceValue = replaceValues[0][4]
    
        answer = answer - firstKeep[K-1][2] + max(firstKeep[K-1][2], biggestReplaceValue)
    
    if doPrint: print "answer = ", answer
            
    if doPrint: print " "
    if doPrint == False: print "case #" + str(i+1) + ": " + str(answer)
    