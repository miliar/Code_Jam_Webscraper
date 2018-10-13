t = int(raw_input())  # read a line with a single integer

import numpy as np

for i in xrange(1, t + 1):
    N, nR, nO, nY, nG, nB , nV  = [s for s in raw_input().split(" ")]
    N = int(N) #total number of horses
    nR = int(nR) #number of red horses
    nO = int(nO)
    nY = int(nY)
    nG = int(nG)
    nB = int(nB)
    nV = int(nV)

    #this is the reduced number of red horses, taking into account the fact that
    #any Green horse must be surrounded by R horses, similar for O and V
    reducR = nR - nG
    reducY = nY - nV
    reducB = nB - nO

    to_sort = [reducR, reducY,reducB]
    to_sort.sort()
    [l, m, n] = to_sort
    if (n==reducR):
        nChar = "R"
        if (m==reducY):
            mChar = "Y"
            lChar = "B"
        elif(m==reducB):
            mChar = "B"
            lChar = "Y"
    elif (n==reducY):
        nChar = "Y"
        if (m==reducR):
            mChar = "R"
            lChar = "B"
        elif(m==reducB):
            mChar = "B"
            lChar = "R"
    elif (n==reducB):
        nChar = "B"
        if (m==reducR):
            mChar = "R"
            lChar = "Y"
        elif(m==reducY):
            mChar = "Y"
            lChar = "R"

    one_cols = [nR, nY, nB]
    numZeros = 0
    for j in range(0,3):
        if one_cols[j]==0:
            numZeros = numZeros + 1

    if( (n > l+m) or n<0 or m<0 or l<0):
        #the task is impossible
        print "Case #{}: {}".format(i, "IMPOSSIBLE")
    elif(numZeros==2 and n==0 and m==0 and l==0):
        order = []
        if nR != 0:
            for j in range(0,nR):
                order.append("R")
                order.append("G")
        if nY != 0:
            for j in range(0,nY):
                order.append("Y")
                order.append("V")
        if nB != 0:
            for j in range(0,nB):
                order.append("B")
                order.append("O")
        print "Case #{}: {}".format(i, ''.join(order))
    elif(numZeros < 2 and n==0 and m==0 and l==0):
        print "Case #{}: {}".format(i, "IMPOSSIBLE")
    else:
        order = []
        unsorted = [reducR, reducY,reducB]

        while(n + m + l > 0):
            if (m > l):
                #reduce n and m by 1
                order.append(nChar)
                order.append(mChar)
                n = n-1
                m = m-1
            elif(m==l and n>m):
                #reduce m and l by 1, n by 2
                order.append(nChar)
                order.append(mChar)
                order.append(nChar)
                order.append(lChar)
                n = n-2
                m = m-1
                l = l-1
            elif(m==l and m==n):
                #reduce m, l and n by 1
                order.append(nChar)
                order.append(mChar)
                order.append(lChar)
                n = n-1
                m = m-1
                l = l-1

        #now add in the double coloured horses
        #orange
        if(nO>0):
            replaced=False
            j=0
            while(replaced==False):
                if order[j]=="B":
                    replaced = True
                    for k in range(0,nO):
                        order[j] = order[j] + "OB"
                j=j+1

        #Green
        if(nG>0):
            replaced=False
            j=0
            while(replaced==False):
                if order[j]=="R":
                    replaced = True
                    for k in range(0,nG):
                        order[j] = order[j] + "GR"
                j=j+1

        #violet
        if(nV>0):
            replaced=False
            j=0
            while(replaced==False):
                if order[j]=="Y":
                    replaced = True
                    for k in range(0,nG):
                        order[j] = order[j] + "VY"
                j=j+1


        print "Case #{}: {}".format(i, ''.join(order))
