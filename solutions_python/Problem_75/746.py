fin = open("B-small-attempt0.in")
fout = open("B-output.txt", "wt")
testCnt = int(fin.readline())

for i in range(0, testCnt):
    strItems = fin.readline().strip().split(" ")

    pairCnt = int(strItems[0])
    pairs = {}
    if pairCnt>0:
        pairList = strItems[1:pairCnt+1];
        for pair in pairList:
            if pair[0]<pair[1]:
                pairName = pair[0] + pair[1]
            else:
                pairName = pair[1] + pair[0]
            pairs[pairName] = pair[2]
        
    opposedCnt = int(strItems[pairCnt+1])
    opposedPairs = {}
    if opposedCnt>0:
        opposedList = strItems[pairCnt+2:pairCnt+2+opposedCnt]
        for opposed in opposedList:
            opposedPairs[opposed[0]] = opposed[1]
            opposedPairs[opposed[1]] = opposed[0]
    series = strItems[-1]
    stack = []
    occurances = {}
    for element in series:
        stack.append(element)
        if occurances.has_key(element)==False:
            occurances[element] = 0
        occurances[element] += 1
        while True:
            changed = False
            if len(stack)<2:
                break
            leftItem = stack[-2]
            curItem = stack[-1]
            if leftItem<curItem:
                lastPair = leftItem + curItem
            else:
                lastPair = curItem + leftItem
            #print "Lastpair: " + lastPair + ", [" + "".join(stack) + "]"
            # Handle together pairs:
            if pairs.has_key(lastPair):
                if occurances.has_key(pairs[lastPair])==False:
                    occurances[pairs[lastPair]] = 0
                occurances[stack[-1]] -=1
                occurances[stack[-2]] -=1
                occurances[pairs[lastPair]] += 1
                stack.pop()
                stack.pop()
                stack.append(pairs[lastPair])
                curItem = stack[-1]
                changed = True
                #print "Replace with " + curItem + ", [" + "".join(stack) + "]"
            # Handle opposing pairs
            if opposedPairs.has_key(curItem):
                opposingItem = opposedPairs[curItem]
                if occurances.has_key(opposingItem) and occurances[opposingItem]>0:
                    #print "Opposed " + curItem + ", clean" +", [" + "".join(stack) + "]"
                    stack = []
                    occurances = {}
                    changed = True
            if changed:
                continue
            break

    string = "Case #%d: [%s]\n" % (i+1, ", ".join(stack))
    fout.write(string)
    print string
    
print "OK"
fin.close()    
fout.close()
