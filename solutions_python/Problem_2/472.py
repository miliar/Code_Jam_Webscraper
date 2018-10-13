# Google Code Jam
# Simon Tan
# simtanx@gmail.com

# Takes in a time string in format 'hh:mm' and converts it to an integer representing minutes from 00:00
def toMinutes(time):
    [hours, minutes] = time.split(':')
    return (60*int(hours))+int(minutes)

# Given a ready time at one station, checks the other station's schedule to see the soonest return trip
def findSoonestReturnTrip(readyToGoTime, schedule):
    #print "Ready to go at " + str(readyToGoTime)
    for trip in schedule:
        if readyToGoTime <= trip[0]:
    #        print "Taking this trip back: " + str(trip)
            return trip
    #print "Failed to find a trip back, train stays."
    return None

def runOneTrain(schedA, schedB, nTurnaround):
    #print "a->b trips left: " + str(schedA)
    #print "b->a trips left: " + str(schedB)
    trip = None
    otherSched = None
    
    # Most confusing decision ever
    if len(schedA) == 0:
        if len(schedB) == 0:
    #        print 'case 1'
            return None
        else:
    #        print 'case 2'
            trip = schedB.pop(0)
            otherSched = schedA
    else:
        if len(schedB) == 0:
    #        print 'case 3'
            trip = schedA.pop(0)
            otherSched = schedB
        else:
            # Comparison case
            if schedA[0][0] < schedB[0][0]:
    #            print 'case 4'
                trip = schedA.pop(0)
                otherSched = schedB
            elif schedA[0][0] > schedB[0][0]:
    #            print 'case 5'
                trip = schedB.pop(0)
                otherSched = schedA
            else:
    #            print 'case 6'
                # Their first nodes have the same starting time
                if schedA[0][1] <= schedB[0][1]:
                    trip = schedA.pop(0)
                    otherSched = schedB
                else:
                    trip = schedB.pop(0)
                    otherSched = schedA
    
    #print "is otherSched ... B? "  + str (otherSched is schedB)
    origTrainLocation = 'A' if (otherSched is schedB) else 'B'
    
    trip = findSoonestReturnTrip(trip[1]+nTurnaround, otherSched)
    while trip:
        otherSched.remove(trip)
        otherSched = schedB if (otherSched == schedA) else schedA
        trip = findSoonestReturnTrip(trip[1]+nTurnaround, otherSched)

    #print "Done with one train that started at " + origTrainLocation

    return origTrainLocation

# Open file and determine number of cases
input = open('B-large.in','r')
nCases = int(input.readline())

# Iterate through cases
for case in range(nCases):
    
    # Read in turn time and number of A->B and B->A trips
    nTurntime = int(input.readline())
    #print "Turnaround time for this case: " + str(nTurntime)
    [nA, nB] = input.readline().split()
    
    # Read in A->B trips
    lABTrips = []
    for nATrip in range(int(nA)):
        [depart, arrive] = input.readline().split()
        lABTrips.append( (toMinutes(depart), toMinutes(arrive)) )
    
    # Read in B->A trips
    lBATrips = []
    for nBTrip in range(int(nB)):
        [depart, arrive] = input.readline().split()
        lBATrips.append( (toMinutes(depart), toMinutes(arrive)) )
    
    lABTrips.sort()
    lBATrips.sort()
    
    #print "a->b trips: " + str(lABTrips)
    #print "b->a trips: " + str(lBATrips)
    

    nATrains = 0
    nBTrains = 0
    
    result = runOneTrain(lABTrips, lBATrips, nTurntime)
    while result:
        if result == 'A':
            nATrains += 1
        elif result == 'B':
            nBTrains += 1
        else:
            print "WHAT HAPPENED TO RUNONETRAIN?"
        
        result = runOneTrain(lABTrips, lBATrips, nTurntime)
    
    print "Case #" + str(case+1) + ": " + str(nATrains) + " " + str(nBTrains)
        
input.close()