"""Train test 1 
   Google CodeJam 2008
"""

from datetime import datetime, timedelta

def getnextstation(trips):
    if not trips[0]:
        return 1
    if not trips[1]:
        return 0
    x = trips[0][0][1]
    y = trips[1][0][1]
    if x < y:
        return 0
    if x > y:
        return 1
    print "Backtracking needed?! ", x, y
    return 0 #todo choose one with best next move...

def routine(trips, turnaround):
    print "Turnaround =", turnaround
    
    trains = [0, 0]
    
    while any(trips):
        station = getnextstation(trips)
        t = trips[station][0][0]
        trains[station] += 1
        print "New train starting from", station
        trip = 0
        while trip < len(trips[station]):
            if trips[station][trip][0] >= t:
                #journey
                print "\tTaking trip from", station, "to", 1-station, "using", trips[station][trip][0].strftime('%H:%M'), "-", trips[station][trip][1].strftime('%H:%M')
                t = trips[station][trip][1] + turnaround
                del trips[station][trip]
                station = 1 - station  #flip-flop
                trip = 0
            else:
                trip += 1
    
    return "%d %d" % (trains[0], trains[1])


if __name__ == '__main__':
    filename = "B-small-attempt1"
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")
    
    n = int(f.readline())
    print n, "cases"
    for i in range(n):
        turnaround = int(f.readline())
        turnaround = timedelta(0, turnaround * 60)
        
        tripn = [int(tripstation) for tripstation in f.readline().split()]        
        
        trips = []
        for station in (0,1):
            stationtrips = []
            for trip in range(tripn[station]):
                starts, stops  = f.readline().split()
                start = datetime(2008,07, 17, int(starts.split(':')[0]), int(starts.split(':')[1]))
                stop = datetime(2008, 07, 17, int(stops.split(':')[0]), int(stops.split(':')[1]))
                stationtrips.append((start, stop))
            #stationtrips.sort(lambda x,y: cmp(x[1], y[1]))
            stationtrips.sort(lambda x,y: cmp(x[0], y[0]))
            trips.append(stationtrips)
        
        print
        print >>fo, "Case #%d: %s" % (i+1, routine(trips, turnaround))
    
    fo.close()
    f.close()
