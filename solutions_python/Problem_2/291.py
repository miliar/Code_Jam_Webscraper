import math
import re

fp = open('B-large.in.txt')

totalCases = int(fp.readline())

def addWaitTime(wt, t):
    (h, m) = t.split(":")
    (h, m) = map(int, (h, m))
    m += wt
    if m >= 60:
        m = m % 60
        h += 1
    return "%s:%s" % (h, m)

def compareDeparture(t1, t2):
    (h1, m1) = t1.split(":")
    (h2, m2) = t2.split(":")
    (h1, m1, h2, m2) = map(int, (h1, m1, h2, m2))
    if h2 > h1:
        return 1
    elif h2 < h1:
        return -1
    else:
        if m2 > m1:
            return 1
        elif m2 < m1:
            return -1
    return 0
    

for case in range(0, totalCases):
    waitTime = int(fp.readline())
    trainCount = fp.readline().split(" ")
    trainCount = map(int, trainCount)
    trains = []
    # (0A/1B, depart, arrive)
    for a in range(0, trainCount[0]):
        line = fp.readline().replace("\n", "")
        line = line.replace("\r", "")
        (depart, arrive) = line.split(" ")
        inserted = False
        for t in range(0, len(trains)):
            if not inserted and compareDeparture(trains[t][1], depart) == -1:
                trains.insert(t, (0, depart, arrive))
                inserted = True
        if not inserted:
            trains.append((0, depart, arrive))
    for b in range(0, trainCount[1]):
        line = fp.readline().replace("\n", "")
        line = line.replace("\r", "")
        (depart, arrive) = line.split(" ")
        inserted = False 
        for t in range(0, len(trains)):
            if not inserted and compareDeparture(trains[t][1], depart) == -1:
                trains.insert(t, (1, depart, arrive))
                inserted = True
        if not inserted:
            trains.append((1, depart, arrive))
    
    tl = ([], []) # [ time ready ]
    needTrains = [0, 0]
    
    for train in trains:
        (st, depart, arrive) = train
        foundTrain = False
        for t in tl[st]:
            if not foundTrain and compareDeparture(t, depart) >= 0:
                foundTrain = True
                tl[st].remove(t)
        if not foundTrain:
            needTrains[st] += 1
        # send train to other station
        tl[(st + 1) % 2].append(addWaitTime(waitTime, arrive))
    
    print "Case #%i: %i %i" % (case + 1, needTrains[0], needTrains[1])

fp.close()
