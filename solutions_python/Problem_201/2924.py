#!/usr/bin/python

import math

input = open('inputC.in', 'r')
output = open('outputC.out', 'w')

cases = int(input.readline())
#print 'Casos: '+ str(cases)

t = 0
while (t < cases):

    ##print "Case: "+str(t+1)

    line = input.readline()

    n = int(line.split(" ")[0])
    k = int(line.split(" ")[1])

    #print "n: "+str(n)
    #print "k: "+str(k)

    stalls = []
    for i in range(n+2):
        stalls.append(0)
    stalls[0] = 1
    stalls[n+2-1] = 1

    #print stalls

    if n == k:
        out = "Case #"+str(t+1)+": "+str(0)+" "+str(0)+"\n";
        #print out
        output.write(out)
    else:
        for i in range(k):
            emptyStalls = []
            #print "--- Ciclo i:"+str(i)

            for j in range(len(stalls)):
                #print "j:"+str(j)
                val = stalls[j]
                #print "val: "+str(val)

                if(val == 0):
                    ls = 0
                    p = 1
                    while j-p >= 0:
                        if stalls[j-p] == 0:
                            ls += 1
                        else:
                            break
                        p += 1
                    rs = 0
                    p = 1
                    while j+p < len(stalls):
                        if stalls[j+p] == 0:
                            rs += 1
                        else:
                            break
                        p += 1
                    emptyStalls.append([ls,rs])
                    #print "ls: "+str(ls)
                    #print "rs: "+str(rs)
                else:
                    emptyStalls.append(0)

            #print emptyStalls

            minV = []
            maxV = []
            for j in range(len(emptyStalls)):
                if emptyStalls[j] != 0:
                    minV.append(emptyStalls[j][0] if emptyStalls[j][0]<emptyStalls[j][1] else emptyStalls[j][1])
                    maxV.append(emptyStalls[j][0] if emptyStalls[j][0]>emptyStalls[j][1] else emptyStalls[j][1])
                else:
                    minV.append(None)
                    maxV.append(None)

            #print minV
            #print maxV

            maxminV = max(minV)
            maxmaxV = max(maxV)

            #print maxminV
            #print maxmaxV

            maxLsRs = None
            minLsRs = None

            minLsRsIndex = []

            minIndex = 0;
            minCount = 0;
            for j in range(len(minV)):
                if minV[j] != None:
                    if(minV[j] == maxminV):
                        minIndex = j
                        minCount += 1
                        minLsRsIndex.append(minIndex)
            #print "minCount: "+str(minCount)
            #print "minIndex: "+str(minIndex)
            #print "minLsRsIndex: "+str(minLsRsIndex)

            if(minCount == 1):
                stalls[minIndex] = 1;
                maxLsRs = max(emptyStalls[minIndex])
                minLsRs = min(emptyStalls[minIndex])
            else:
                newV = []
                for p in range(len(minLsRsIndex)):
                    newV.append(maxV[minLsRsIndex[p]])

                #print "newV: "+str(newV)

                maxnewV = max(newV)

                maxLsRsIndex = []
                maxIndex = 0
                maxCount = 0
                for j in range(len(newV)):
                    if(newV[j] == maxnewV):
                        maxIndex = j
                        maxCount += 1
                        maxLsRsIndex.append(minLsRsIndex[maxIndex])

                #print maxLsRsIndex

                if(maxCount == 1):
                    stalls[maxIndex] = 1;
                    maxLsRs = max(emptyStalls[maxIndex])
                    minLsRs = min(emptyStalls[maxIndex])
                else:
                    leftmostIndex = min(maxLsRsIndex)
                    #print "leftmostIndex: "+str(leftmostIndex)
                    stalls[leftmostIndex] = 1;
                    maxLsRs = max(emptyStalls[leftmostIndex])
                    minLsRs = min(emptyStalls[leftmostIndex])

            #print stalls

        out = "Case #"+str(t+1)+": "+str(maxLsRs)+" "+str(minLsRs)+"\n";
        #print out
        output.write(out);

    t = t + 1

output.close()
