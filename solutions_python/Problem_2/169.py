#!/usr/bin/python

import logging

CurrentDebugLevel=logging.DEBUG

def CompareTime(x, y):
    if x[0] == y[0]: # hour same
        return x[1] - y[1]
    else: return x[0] - y[0]

def CountTrain(leaveTime, arriveTime, turnAroundTime):
    count = 0
    # add turnAroundTime
    for iTime in arriveTime:
        iTime[1] += turnAroundTime
        if iTime[1] >= 60:
            iTime[1] -= 60
            iTime[0] += 1
    #logging.debug(arriveTime)
    idxLeave = 0 
    idxArrive = 0
    while idxLeave < len(leaveTime) and idxArrive < len(arriveTime):
        ret = CompareTime(leaveTime[idxLeave], arriveTime[idxArrive])
        if ret < 0: count += 1 # not enough train
        else: 
            idxArrive += 1 # we have one train at least
        idxLeave += 1
    count += (len(leaveTime) - idxLeave) 
    return count

def ProcessCase(leaveTimeAtA, arriveTimeAtB, leaveTimeAtB, arriveTimeAtA, turnAroundTime):
    leaveTimeAtA.sort(CompareTime)
    arriveTimeAtB.sort(CompareTime)
    leaveTimeAtB.sort(CompareTime)
    #logging.debug(arriveTimeAtA)
    arriveTimeAtA.sort(CompareTime)
    trainInA = CountTrain(leaveTimeAtA, arriveTimeAtA, turnAroundTime)
    trainInB = CountTrain(leaveTimeAtB, arriveTimeAtB, turnAroundTime)
    return (trainInA, trainInB)

def OutputResult(caseNum, outFile, result):
    outFile.write('Case #%d: %d %d\n' % (caseNum, result[0], result[1]))

def ProcessDataFile(fileName):
    inFile = open(fileName, 'r')
    line = inFile.readline()
    lineCount = int(line)
    
    leaveTimeAtA = []
    arriveTimeAtB = []
    leaveTimeAtB = []
    arriveTimeAtA = []
    outFile = open(fileName + '.out.txt', 'w')
    for i in xrange(1, lineCount + 1):
        line = inFile.readline()
        turnAroundTime = int(line)
        logging.debug('Case %d', i)

        line = inFile.readline()
        counts = line.strip().split()
        numA = int(counts[0])
        numB = int(counts[1])
        for j in xrange(numA):
            line = inFile.readline()
            time = line.strip().split()
            leaveTimeAtA.append([int(x) for x in time[0].split(':')])
            arriveTimeAtB.append([int(x) for x in time[1].split(':')])
        for j in xrange(numB):
            line = inFile.readline()
            time = line.strip().split()
            leaveTimeAtB.append([int(x) for x in time[0].split(':')])
            arriveTimeAtA.append([int(x) for x in time[1].split(':')])
            
        result = ProcessCase(leaveTimeAtA, arriveTimeAtB, leaveTimeAtB, arriveTimeAtA, turnAroundTime)
        logging.debug('%d %d' % result)
        leaveTimeAtA = []
        arriveTimeAtB = []
        leaveTimeAtB = []
        arriveTimeAtA = []
        OutputResult(i, outFile, result)
    outFile.close()

def main():
    logging.basicConfig(level=CurrentDebugLevel, datefmt='%Y.%m.%d %H:%M:%S', format='%(asctime)s %(levelname)-5s %(message)s')
    
    #ProcessDataFile('B-small.txt')
    #ProcessDataFile('B-small-attempt0.in')
    ProcessDataFile('B-large.in')

if __name__ == '__main__': main()