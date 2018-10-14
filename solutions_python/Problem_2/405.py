#!/usr/bin/python
from  datetime import datetime, timedelta


class Train:
    def __init__(self,start):
        self.start_loc = start
        self.arrival = None
        self.avail = False
        self.intransit = False


basetime = datetime.today().date()

f = open('A-small.in')


test_cases = int(f.readline().strip())

case_num = 1

for i in range(test_cases):
    a_count = 0
    b_count = 0
    a_jobs = []
    b_jobs = []
    trains = {}
    trains['a'] = []
    trains['b'] = []
    
    turnaround = int(f.readline().strip())
    
    a_trips, b_trips = [ int(x) for x in f.readline().strip().split() ]

    for a in range(a_trips):
        depart, arrive = f.readline().strip().split()
        a_jobs.append( ( datetime.strptime(depart, '%H:%M'), datetime.strptime(arrive, '%H:%M') )   )

    for b in range(b_trips):
        depart, arrive = f.readline().strip().split()
        b_jobs.append( ( datetime.strptime(depart, '%H:%M'), datetime.strptime(arrive, '%H:%M') )   )
    starts = [ s[0] for s in a_jobs  + b_jobs ] 
    starts.sort()
    for s in starts:
        for t in trains['a']:
            if (t.arrival + timedelta(minutes= turnaround)) <= s and not t.avail:
                t.avail = True
                trains['a'].remove(t)
                trains['b'].append(t)
        for t in trains['b']:
            if (t.arrival + timedelta(minutes= turnaround)) <= s and not t.avail:
                t.avail = True
                trains['b'].remove(t)
                trains['a'].append(t)
        for j in a_jobs:
            if j[0] <= s:
                the_train = False
                for t in trains['a']:
                    if t.avail:
                        the_train = t
                        break
                if not the_train:
                    a_count += 1      
                    the_train = Train('a')
                    trains['a'].append(the_train)
                the_train.avail = False
                the_train.arrival = j[1]
                a_jobs.remove(j)
        for j in b_jobs:
            if j[0] <= s:
                the_train = False
                for t in trains['b']:
                    if t.avail:
                        the_train = t
                        break
                if not the_train:
                    b_count += 1      
                    the_train = Train('b')
                    trains['b'].append(the_train)
                the_train.avail = False
                the_train.arrival = j[1]
                b_jobs.remove(j)
    #for s in starts:
    print "Case #%d: %d %d" % (case_num, a_count, b_count)
         
    case_num += 1
    #for j in range(qs):
    #    queries.append(f.readline().strip())
#    conflicts = [ x for x in search_engines if x not in queries ]
#    print conflicts
#    if conflicts:
#        print "Case #%d: 0" % (case_num,)
#        continue
    #queue = search_engines[:]
    #for q in queries:
    #    if q in queue:
    #        queue.remove(q)
    #    if len(queue) == 0:
    #        switches += 1
    #        queue = search_engines[:]
    #        queue.remove(q)
