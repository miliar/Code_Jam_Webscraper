def schedule_events(timeline, dep, ready, origin, dest):
    if not timeline.has_key(dep):
        timeline[dep] = []
    timeline[dep].append( ('C', origin) )        
        
    if not timeline.has_key(ready):
        timeline[ready] = []
    timeline[ready].insert(0, ('P', dest))        

N = int(raw_input())
case_number = 0

for i in xrange(N):
    timeline = {}
    T = int(raw_input())
    NA, NB = map(int, raw_input().split())
    
    for j in xrange(NA):
        departure, arrival = raw_input().split()
        dep_hour, dep_min = map(int, departure.split(":"))
        arr_hour, arr_min = map(int, arrival.split(":"))
        schedule_events(timeline, dep_hour*60 + dep_min, arr_hour *60 + arr_min + T, 'A', 'B')
        
    for j in xrange(NB):
        departure, arrival = raw_input().split()
        dep_hour, dep_min = map(int, departure.split(":"))
        arr_hour, arr_min = map(int, arrival.split(":"))
        schedule_events(timeline, dep_hour*60 + dep_min, arr_hour *60 + arr_min + T, 'B', 'A')
    
    min_trains   = {'A':0, 'B':0}
    avail_trains = {'A':0, 'B':0}
    
    for time in sorted(timeline.keys()):
        events = timeline[time]
        
        for event in events:
            if event[0] == 'P':
                avail_trains[event[1]] += 1
            if event[0] == 'C':
                if avail_trains[event[1]] == 0:
                    min_trains[event[1]] += 1
                else:
                    avail_trains[event[1]] -= 1
    
    case_number += 1
    print "Case #%d: %d %d" % (case_number, min_trains['A'], min_trains['B'])