from __future__ import print_function
import sys

# print to stderr for debugging
enableDebug = True
def printe(*stuff):
    if enableDebug:
        print(*stuff, file=sys.stderr) 


# Open file for processing
filename = sys.argv[1]
inputFile = open(filename, 'r')
lines = [l.rstrip('\n') for l in inputFile]
linesIter = iter(lines)
nCases = int(linesIter.next())


# Process each case
for iCase in range(1,nCases+1):
    # printe("\nProcessing case " + str(iCase))

    # Solve problem
    items = linesIter.next().split(' ')
    nSeats = int(items[0])
    nPeople = int(items[1])
    nTickets = int(items[2])

    tickets = []
    personTrainCount = [0] * nPeople
    for i in range(nTickets):
        items = linesIter.next().split(' ')
        pos = int(items[0])-1
        ID = int(items[1])-1
        tickets.append((pos,ID))
        personTrainCount[ID] += 1

    tickets.sort()

    minTrain = 0
    for c in personTrainCount:
        minTrain = max((minTrain, c))

    # Pack densely to count trains
    nTrains = minTrain
    excessSeats = 0
    iTick = 0
    for iSeat in range(nSeats):

        excessSeats += nTrains
        
        # Place people
        while(iTick < len(tickets) and tickets[iTick][0] == iSeat):

            if(excessSeats == 0):
                nTrains += 1
                excessSeats += iSeat + 1

            excessSeats -= 1
            iTick += 1

    # printe("nTrains = {}".format(nTrains))


    nPromo = 0 
    excessSeats = 0
    iTick = 0
    for iSeat in range(nSeats):

        nThisRow = nTrains
        
        # Place people
        while(iTick < len(tickets) and tickets[iTick][0] == iSeat):

            if(nThisRow > 0):
                nThisRow -= 1
            elif(excessSeats > 0):
                excessSeats -= 1
                nPromo += 1
            else:
                print("ERROR ERROR")

            iTick += 1

        excessSeats += nThisRow

    print("Case #{}: {} {}".format(iCase, nTrains, nPromo))
