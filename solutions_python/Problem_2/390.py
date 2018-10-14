class Time:
    
    def __init__(self, s, t=None):
        self.hour = 0
        self.minute = 0
        self.turnaroundTime = t
        self.parse(s)
        
        if t:
            self.minute += t
        
        if self.minute >= 60:
            self.hour += self.minute / 60
            self.minute = self.minute % 60
            
    def parse(self, s):
        s = s.split(':')
        self.hour = int(s[0])
        self.minute = int(s[1])

    def getTime(self):
        return (self.hour, self.minute)
    
    def __str__(self):
        return '<Time %d:%d>' % (self.hour, self.minute)
    
        
class Station:
    
    def __init__(self):
        self.trains = 0
        self.availableTrains = 0
        self.arrivals = []
        self.departures = []
        
    def addArrivalTime(self, t):
        self.arrivals.append(t)
        self.arrivals.sort(cmp=timecompare)
#        print 'arrivals:'
#        for k in self.arrivals:
#            print '-%s' % str(k)
        
    def addDepartureTime(self, t):
        self.departures.append(t)
        self.departures.sort(cmp=timecompare)
      #  print 'departures:'
        #for k in self.departures:
      #      print '-%s' % str(k)

    def getAvailableTrains(self):
        i = 0
        for a in self.departures:
            # PAra cada horario de chegada
            first = None
            # Primeiro
            if len(self.arrivals) > i:
                first = self.arrivals[i]
            else:
                first = None
            
            if not first or a.getTime() < first.getTime():
                self.trains += 1
            else:
                i += 1
        return self.trains
        

def timecompare(t1, t2):
    (t1Hour, t1Minute) = t1.getTime()
    (t2Hour, t2Minute) = t2.getTime()
    
    if t1Hour > t2Hour:
        return 1
    
    if t1Hour < t2Hour:
        return -1
    
    if t1Hour == t2Hour:
        if t1Minute > t2Minute:
            return 1
        elif t1Minute < t2Minute:
            return -1
        else:
            return 0


class StationManager:
    
    def __init__(self, t):
        self.turnaround = t
        
    def solve(self, stationA, stationB):

        return (stationA.getAvailableTrains(), stationB.getAvailableTrains())
    
    
def getSchedule(turnaroundTime):
    r = str(raw_input())
    r = r.split(' ')
    left = r[0]
    right = r[1]
    
    right = Time(right, turnaroundTime)  
    left = Time(left)
    return left, right
    
if __name__ == "__main__":
    cases = int(raw_input())
    
    for i in range(1, cases+1):
        A = Station()
        B = Station()
        turnaroundTime = int(raw_input())
        
        na_nb = str(raw_input())
        na_nb = na_nb.split(' ')
        na = int (na_nb[0])
        nb = int (na_nb[1])
        
        for j in range(1, na+1):
            (left, right) = getSchedule(turnaroundTime)
            B.addArrivalTime(right)
            A.addDepartureTime(left)
            
        for j in range(1, nb+1):
            (left, right) = getSchedule(turnaroundTime)
            A.addArrivalTime(right)
            B.addDepartureTime(left)

        k1, k2 = StationManager(turnaroundTime).solve(A,B)
        print 'Case #%d: %d %d' % (i, k1, k2)
        
        
           