import string
def getline(f):
    return string.split(f.readline(), "\n")[0]
    
class Time():
    def __init__(self, str="00:00"):
    
        self.hour = string.atoi(string.split(str, ":")[0])
        self.min  = string.atoi(string.split(str, ":")[1])
        
    def __lt__(self, other):
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour:
            if self.min < other.min:
                return True
        
        return False
        
    def __le__(self, other):
        return self.__lt__(other) or (self.min == other.min and self.hour == other.hour)
        
        
    def __add__(self, other):
        t = Time()
        t.hour = self.hour
        t.min = self.min
            
        if isinstance(other, Time):
            t.min += other.min
            if t.min >= 60:
                t.min -= 60
                t.hour += 1
            t.hour += other.hour
            return t
        elif isinstance(other, int):
            t.min += other
            while t.min >= 60:
                t.min -= 60
                t.hour += 1
            return t
        else:
            raise NotImplemented   
            
    def __str__(self):
        return "%2d:%2d" % (self.hour, self.min)
    
infile = open("B-large.in", 'r')
outfile = open("B-large.out",'w')
numCases = eval(getline(infile))

for case in range(numCases):
    AB={}
    BA={}
    
    turnAroundTime = eval(getline(infile))
    l = string.split(getline(infile))
    
    aTrips = eval(l[0])
    bTrips = eval(l[1])
    
    for i in xrange(aTrips):
        l = string.split(getline(infile))
        AB[Time(l[0])] = Time(l[1])
        
    for i in xrange(bTrips):
        l = string.split(getline(infile))
        BA[Time(l[0])] = Time(l[1])
        
    aSorted = AB.keys()
    bSorted = BA.keys()
    
    aSorted.sort()
    bSorted.sort()

    trainsStartA = 0
    trainsStartB = 0
    
    bTrains = []
    aTrains = []
    while aSorted and bSorted:
        if aSorted[0] < bSorted[0]:
            start = aSorted.pop(0)
            if aTrains and aTrains[0] <= start:
                aTrains.pop(0)
            else:
                trainsStartA += 1
            bTrains.append(AB[start] + turnAroundTime)
            bTrains.sort()
        else:
            start = bSorted.pop(0)
            if bTrains and bTrains[0] <= start:
                bTrains.pop(0)
            else:
                trainsStartB += 1
            aTrains.append(BA[start] + turnAroundTime)
            aTrains.sort()        

    while aSorted:
        start = aSorted.pop(0)
        if aTrains and aTrains[0] <= start:
            aTrains.pop(0)
        else:
            trainsStartA += 1
    
    while bSorted:
        start = bSorted.pop(0)
        if bTrains and bTrains[0] <= start:
            bTrains.pop(0)
        else:
            trainsStartB += 1
            
    outfile.write("Case #%d: %d %d\n" % (case + 1, trainsStartA, trainsStartB))
    