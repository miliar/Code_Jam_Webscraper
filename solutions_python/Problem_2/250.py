from datetime import datetime
from dateutil.relativedelta import relativedelta

FROM_A = 0
FROM_B = 1 



class TimeTableEntry(object):
    def __init__(self, departure_arrival, turnaround, from_where):
        self.departure = self.parse_time(departure_arrival[0])
        self.arrival = self.parse_time(departure_arrival[1])
        self.ready = self.arrival + relativedelta(minutes=turnaround)
        self.from_where = from_where
        self.to_station = FROM_A if from_where == FROM_B else FROM_B
    
    def parse_time(self, time):
        hours,minutes = map(int, time.split(":"))
        return datetime(1970,1,1) + relativedelta(hours=hours, minutes=minutes)
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return "%d| %s => %s  (%s) " % (self.from_where, self.departure, self.arrival, self.ready)
        
class Case(object):
    
    def __init__(self, file):
        self.turnaround = int(file.readline())
        self.num_from_a, self.num_from_b = map(int, file.readline().split(" "))
         

        self.from_a = [ TimeTableEntry( file.readline().split(" "), self.turnaround, FROM_A) 
                       for cnt in xrange(self.num_from_a)]
        
        self.from_b = [ TimeTableEntry( file.readline().split(" "), self.turnaround, FROM_B) 
                       for cnt in xrange(self.num_from_b)]
    
    def solve(self):
        
        trains = [0,0] # FROM_A FROM_B
        
        departures = []
        departures.extend(self.from_a)
        departures.extend(self.from_b)
        
        departures.sort(lambda a, b: cmp(a.departure, b.departure))
        while len(departures):
            where, departures = self.add_train(departures)
            trains[where] += 1
            
                    
        return trains
    
    def add_train(self, departures):
        """
        Adds a train at the earliest needed departure and crosses
        out all subsequent departures that this train can manage
        @param departures:
        """
        current = departures[0]
        del(departures[0])
        added_from = current.from_where        
        for departure_index in xrange(len(departures)):
            next = departures[departure_index]
            if next.from_where == current.to_station and next.departure >= current.ready:
                current = next
                departures[departure_index] = None
        remaining = [departure for departure in departures if departure is not None ]
        return added_from, remaining                              
        
    

if __name__ == '__main__':
    
    file = 'test2.txt'
    file = 'B-small-attempt0.in'
    file = 'B-large.in'
    fp = open(file, 'rb')
    num_cases = int(fp.readline())
    
    cases = [ Case(fp)  
                for x in xrange(num_cases) ]
#    print cases[6].solve()
    for case_index in xrange(len(cases)):
        a,b = cases[case_index].solve()
        print "Case #%d: %d %d" % (case_index + 1, a, b)