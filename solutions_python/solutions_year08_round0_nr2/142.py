import sys

def calculate( trips ):
    trains = {"A": 0, "B": 0}
    curtrip = trips[0]
    trips.remove(curtrip)
    trains[curtrip[2]] += 1
    #print "train:", curtrip, 

    while trips:
        for trip in trips[:]:
            #print "(",trip,")"
            if trip[2] != curtrip[2] and trip[0] >= curtrip[1]:
                curtrip = trip
                trips.remove(trip)
                #print curtrip,
                break
        else:
            curtrip = trips[0]
            trips.remove(trips[0])
            trains[curtrip[2]] += 1
            #print
            #print "train:", curtrip
    
    
    
    return trains["A"], trains["B"]
    

def readtrip( f ):
    return [ int(y)*60+int(z) for [y,z] in [x.split(":") for x in f.readline().rstrip().split()]]

def timetable( f ):
    turnaroundtime = int(f.readline())
    tripcounts = [int(x) for x in f.readline().split()]
    trips = []
    for i in range(tripcounts[0]):
        trips.append( readtrip(f) + ["A"] )
    for i in range(tripcounts[1]):
        trips.append( readtrip(f) + ["B"] )

    trips.sort()

    for trip in trips:
        trip[1] += turnaroundtime

    #print turnaroundtime, tripcounts[0], tripcounts[1], trips
    return calculate( trips )

if len(sys.argv) < 2:
    print "usage: %s inputfile" % sys.argv[0]
    exit()
    
inputFile = sys.argv[1]

try:
    casefile = open( inputFile, "r" )
except:
    print "Error opening file: %s" % inputFile
    exit()

cases = int(casefile.readline())

for case in range(1,cases+1):
    (ATrains, BTrains) = timetable( casefile )
    print "Case #%d: %d %d" % (case, ATrains, BTrains ) 
