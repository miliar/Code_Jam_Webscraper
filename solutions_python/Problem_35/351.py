import sys

if __name__ == '__main__':

    inputLines = file(sys.argv[1], 'r').read().strip().split('\n')

    outFP = file(sys.argv[1]+'.out.txt', 'w')

    for caseNO in range(int(inputLines.pop(0))):
        H, W = map(int, inputLines.pop(0).split())

        altitudeArray = list()
        for h in range(H):
            altitudeArray.extend(map(int, inputLines.pop(0).split()))

        altitudeDict = dict()
        for idx in range(H*W):
            altitude = altitudeArray[idx]
            if altitude not in altitudeDict:
                altitudeDict[altitude] = list()
            altitudeDict[altitude].append(idx)

        altitudeIdxSet = set(range(H*W))

        labelList = list()

        altitudeKeys = altitudeDict.keys()
        altitudeKeys.sort()
        altitudeKeys.reverse()
        for altitude in altitudeKeys:
            #print 'altitude', altitude
            for idx in altitudeDict[altitude]:
                #print 'idx', idx

                NWESidx = list()

                if idx-W > -1: NWESidx.append(idx-W)
                if idx%W != 0: NWESidx.append(idx-1)
                if idx%W != W-1: NWESidx.append(idx+1)
                if idx+W < H*W: NWESidx.append(idx+W)
                NWESalt = map(lambda i: altitudeArray[i], NWESidx)

                if len(NWESalt) == 0 or min(NWESalt) >= altitudeArray[idx]:
                    flowIdx = None
                else:
                    flowIdx = NWESidx[NWESalt.index(min(NWESalt))]
                #print 'idx', 'flowIdx', idx, flowIdx

                inLabelSet = False

                while True:
                    try:
                        matchSetIdx = None
                        for i in range(len(labelList)):
                            labelSet = labelList[i]
                            if idx in labelSet or flowIdx in labelSet:
                                labelSet.add(idx)
                                if flowIdx != None: labelSet.add(flowIdx)
                                if matchSetIdx != None:
                                    mergeSet = labelList[matchSetIdx] | labelSet
                                    labelList[matchSetIdx] = mergeSet
                                    labelList.pop(i)
                                    #print 'merge'
                                    raise
                                matchSetIdx = i
                                inLabelSet = True
                    except:
                        continue
                    break
                if not inLabelSet:
                    labelList.append(set([idx, flowIdx] if flowIdx != None else set([idx,])))
                #print labelList

        outFP.write("Case #%i:\n"%(caseNO+1))

        basinList = [0]*(H*W)

        labelBais = 0
        labelLabelList = [False]*len(labelList)
        labelLabelCount = 0
        labelListLen = len(labelList)
        try:
            for idx in range(H*W):
                for idxLabelList in range(labelListLen):
                    if idx in labelList[idxLabelList]:
                        if labelLabelList[idxLabelList] != False: continue
                        labelLabelList[idxLabelList] = '%c'%(ord('a')+labelBais)
                        labelBais += 1
                        labelLabelCount += 1
                        if labelLabelCount == labelListLen: raise
        except:
            pass

        
        for idxLabelList in range(len(labelList)):
            curBasin = labelLabelList[idxLabelList]
            for tIdx in labelList[idxLabelList]:
                basinList[tIdx] = curBasin

        #for idxLabelList in range(len(labelList)):
        #    curBasin = '%c'%(ord('a')+idxLabelList)
        #    for tIdx in labelList[idxLabelList]:
        #        basinList[tIdx] = curBasin
        for h in range(H):
            wLine = ' '.join(basinList[h*W:h*W+W])
            outFP.write(wLine+'\n')

       # for idx in range(H*W):
       #     altitude = altitudeArray[idx]
       #     for labelSet in labelList:
       #         if altitude

