T = int(raw_input().strip())
for i in range(T):
    temp = map(str, raw_input().strip().split(" "))
    N = int(temp[0])
    K = int(temp[1])

    # find highest full binary that is less than K
    minSpace = (N-1)/2
    maxSpace = N/2
    if K > 1:
        tempBin = format(K-1,'b')
        all1s = tempBin
#        print all1s
        for j in range(len(tempBin)):
            if tempBin[j] == "0": 
                all1s = "1" * (len(tempBin)-1)
                break
        all1sInt = int(all1s, 2)
#        print tempBin, all1s, all1sInt
        baseInLastRow = (N-all1sInt) / (all1sInt + 1)
        rem = (N-all1sInt) % (all1sInt + 1)
        lastGap = baseInLastRow
#        print lastGap
        if K-all1sInt <= rem:
            lastGap += 1
#        print lastGap
        minSpace = (lastGap-1) / 2
        maxSpace = lastGap-1-minSpace
#    print maxSpace, minSpace
    


            
    print "case #" + str(i+1) + ": " + str(maxSpace) + " " + str(minSpace)
            
            
    