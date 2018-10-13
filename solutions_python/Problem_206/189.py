from collections import Counter
import math
T = int(raw_input().strip())
for i in range(T):
    doPrint = False
    if doPrint: print "case #: ", i+1
    temp = map(int, raw_input().strip().split(" "))
    D = temp[0]
    N = temp[1]
    horses = []
    for j in range(N):
        temp = map(int, raw_input().strip().split(" "))
        horses.append(temp)
    if doPrint: print "D, N = ", D, N
    if doPrint: print "horses = ", horses

    maxTime = 0.0
    for j in range(N):
        dist = D - horses[j][0]
        time = float(dist) / horses[j][1]
        maxTime = max(maxTime, time)
    answer = float(D) / maxTime

    if doPrint: print "answer = ", answer
        
    
    if doPrint: print " "

    if doPrint == False: print "case #" + str(i+1) + ": " + str(answer)
    