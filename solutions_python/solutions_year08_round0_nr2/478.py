import time

def makeTime(x) :
    tokens = x.split(':')
    return time.gmtime(int(tokens[0])*3600+int(tokens[1])*60)

def timeToSecs(x) :
    return int(time.strftime("%H",x))*3600 + int(time.strftime("%M",x))*60

f = open('B-large.in')
line = f.readline()
line = f.readline().strip()
count = 0
while line != "" :
    count += 1
    turnaround = int(line)
    line = f.readline().strip()
    line = line.split(' ')
    NA = int(line[0])
    NB = int(line[1])
    Atrains = []
    Btrains = []
    for i in range(0,NA) :
        Atrains.append(map(makeTime,f.readline().strip().split(' ')))
    for i in range(0,NB) :
        Btrains.append(map(makeTime,f.readline().strip().split(' ')))
#    print turnaround, NA, NB, Atrains, Btrains

    countA = 0
    countB = 0
    departedTrains = []
    for hour in range(0,24) :
        for minute in range(0,60) :
            now = time.gmtime(hour*3600+minute*60)
            for train in Atrains :
                if train[0] == now :
#                    print "Train departing A",time.strftime("%H:%M",now)                    
                    reuse = False
                    for departedTrain in departedTrains :
                        if (departedTrain[0] == 'A') and (timeToSecs(departedTrain[1]) <= timeToSecs(now)) and (not reuse) :
                            departedTrains.remove(departedTrain)
                            reuse = True
                    if not reuse :
                        countA += 1
                    departedTrains.append(['B',time.gmtime(timeToSecs(train[1])+turnaround*60)])
#                if train[1] == now :
#                    print "Train arriving B",time.strftime("%H:%M",now)
            for train in Btrains :
                if train[0] == now :
#                    print "Train departing B",time.strftime("%H:%M",now)
                    reuse = False
                    for departedTrain in departedTrains :
                        if (departedTrain[0] == 'B') and (timeToSecs(departedTrain[1]) <= timeToSecs(now)) and (not reuse):
                            departedTrains.remove(departedTrain)
                            reuse = True
                    if not reuse :
                        countB += 1    
                    departedTrains.append(['A',time.gmtime(timeToSecs(train[1])+turnaround*60)])
#                if train[1] == now :
#                    print "Train arriving A",time.strftime("%H:%M",now)
    caseStr = "Case #" + str(count) + ":"
    print caseStr, countA, countB
    line = f.readline().strip()

