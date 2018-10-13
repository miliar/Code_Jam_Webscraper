from collections import deque

def ProcessRollercoaster(numRides, capacity, numPassengers, passengerQueue):
    currentFares = 0
    for x in range(numRides):
        currentPassengers = deque([])
        roomLeft = 1
        currentPassengerCount = 0
        while roomLeft == 1:
            if len(passengerQueue) > 0:
                if passengerQueue[0] <= capacity - currentPassengerCount:
                    currentPassengerCount = currentPassengerCount + passengerQueue[0]
                    currentPassengers.append(passengerQueue.popleft())
                else:
                    roomLeft = 0
            else:
                roomLeft = 0
        currentFares = currentFares + currentPassengerCount
        for y in currentPassengers:
            passengerQueue.append(y)
    return str(currentFares)

inFile = open('Sol3.in')
outFile = open('Sol3.out','w')
numCases = int(inFile.readline())
for x in range(numCases):
    caseLine = inFile.readline()
    caseLine1 = caseLine.split()
    caseLine = inFile.readline()
    caseLine2 = caseLine.split()
    passengers = deque([])
    for y in caseLine2:
        passengers.append(int(y))
    print("Case #" + str(x + 1) + ": " + str(passengers))
    outFile.write("Case #" + str(x + 1) + ": " + ProcessRollercoaster(int(caseLine1[0]), int(caseLine1[1]), int(caseLine1[2]), passengers) + "\n")
inFile.close()
outFile.close()