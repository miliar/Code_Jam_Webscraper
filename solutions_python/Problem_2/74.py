PATH_INPUT = 'B-large.in'
PATH_OUTPUT = 'B-code.out'

##import copy
##
##def simTrain(timesSorted, tripsAB, tripsBA, trainsA, trainsB, *f):
##    trainsA = copy.deepcopy(trainsA)
##    trainsB = copy.deepcopy(trainsB)
##    trainsMidway = []
##
##    for time in timesSorted:
##
##        for trip in tripsAB:
##
##            # If a train is to depart from A
##            if time == trip[0]:
##                if not trainsA:             # Not enough trains
##                    return 1
##                trainsA.pop()
##                trainsMidway.append(tripsAB.index(trip) + 1)
##
##            # If a train is to arrive at B
##            if time == trip[1]:
##                trainsMidway.remove(tripsAB.index(trip) + 1)
##                trainsB.append(0)
##
##        for trip in tripsBA:
##
##            # If a train is to depart from B
##            if time == trip[0]:
##                if not trainsB:             # Not enough trains
##                    return 2
##                trainsB.pop()
##                trainsMidway.append(-tripsBA.index(trip) - 1)
##
##            # If a train is to arrive at A
##            if time == trip[1]:
##                trainsMidway.remove(-tripsBA.index(trip) - 1)
##                trainsA.append(0)

        ##DEBUG
        #if len(f):
            #print tripsAB, tripsBA
            #print getTime(time), trainsA, '|', trainsMidway, '|', trainsB
##DEBUG ONLY
##def getTime(time):
##    return "%2i:%2i" % (time / 60, time % 60)

def calculate(T, tripsAB, tripsBA):

    # Add T to each arrival time & get all used times
    timesSet = set([])
    for trip in tripsAB:
        trip[1] += T
        timesSet.add(trip[0])
        timesSet.add(trip[1])
    for trip in tripsBA:
        trip[1] += T
        timesSet.add(trip[0])
        timesSet.add(trip[1])
    times = list(timesSet)
    times.sort()

    trainsARequired = 0
    trainsBRequired = 0
    ##trainsA = []
    ##trainsB = []

    # Simulate the train trip
    trainsA = 0
    trainsB = 0
    trainsMidway = []

    for time in times:

        for trip in tripsAB:

            # If a train is to depart from A
            if time == trip[0]:
                trainsA -= 1
                trainsMidway.append(tripsAB.index(trip) + 1)

            # If a train is to arrive at B
            if time == trip[1]:
                trainsMidway.remove(tripsAB.index(trip) + 1)
                trainsB += 1

        for trip in tripsBA:

            # If a train is to depart from B
            if time == trip[0]:
                trainsB -= 1
                trainsMidway.append(-tripsBA.index(trip) - 1)

            # If a train is to arrive at A
            if time == trip[1]:
                trainsMidway.remove(-tripsBA.index(trip) - 1)
                trainsA += 1

        if trainsA < 0:
            trainsARequired += -trainsA
            trainsA = 0

        if trainsB < 0:
            trainsBRequired += -trainsB
            trainsB = 0

    return trainsARequired, trainsBRequired
            
##    while True:
##        res = simTrain(times, tripsAB, tripsBA, trainsA, trainsB)
##        if res == 1:
##            trainsA.append(0)
##        elif res == 2:
##            trainsB.append(0)
##        else:
##            simTrain(times, tripsAB, tripsBA, trainsA, trainsB, 0)
##            return len(trainsA), len(trainsB)

def time2min(time):
    hours, minutes = time.split(':')
    return int(hours) * 60 + int(minutes)

def main():
    # Load input
    inp = open(PATH_INPUT)
    inpL = inp.readlines()
    inp.close()
    del inp

    # Prepare output
    out = open(PATH_OUTPUT, 'w')
    out.truncate(0)

    mode = 0

    for line in inpL:
        line = line.strip()

        # Load num of cases
        if mode == 0:
            N = int(line)
            case = 0
            mode = 1

        # Load turnaround time
        elif mode == 1:
            case += 1
            T = int(line)
            mode = 2

        # Load num of A->B and B->A trips
        elif mode == 2:
            NA, NB = line.split()
            NA, NB = int(NA), int(NB)

            tripsAB = []
            tripsBA = []

            i = 0
            if NA != 0:
                mode = 3
            elif NB != 0:
                mode = 4
            else:
                mode = 5

        # Load A->B trips
        elif mode == 3:
            depTime, arrTime = line.split()
            tripsAB.append([time2min(depTime), time2min(arrTime)])

            i += 1
            if i == NA:
                i = 0
                if NB != 0:
                    mode = 4
                else:
                    mode = 5

        # Load B->A trips
        elif mode == 4:
            depTime, arrTime = line.split()
            tripsBA.append([time2min(depTime), time2min(arrTime)])

            i += 1
            if i == NB:
                mode = 5

        # Perform computation
        if mode == 5:
            trainsA, trainsB = calculate(T, tripsAB, tripsBA)
            print 'Case #%i: %i %i' % (case, trainsA, trainsB)
            out.write('Case #%i: %i %i\n' % (case, trainsA, trainsB))
            mode = 1

            if case == N:
                break

    out.close()

main()
