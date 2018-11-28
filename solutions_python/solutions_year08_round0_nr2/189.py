from sys import maxint as INF

fd = open('B-large.in', 'r')
s = fd.read()
fd.close()
s = s.split('\n')

num_cases = int(s[0])

s = s[1:]

class TrainTestCase:
    def __init__(self, timeline):
        self.timeline = timeline


# timeline is a list of trainevents

# trainevents indicate arrival, departure and when a train is ready

class TrainEvent:
    def __init__(self, time, loc, type):
        self.time = time
        self.loc = loc
        self.type = type
    def __cmp__(self, other):
        if self.type == 'RDY' and other.type != 'RDY':
            return cmp(self.time-0.00000001, other.time)
        elif self.type != 'RDY' and other.type == 'RDY':
            return cmp(self.time, other.time-0.000001) # these are hacks so train ready's take slight precedence other others in the ordering
        else:
            return cmp(self.time, other.time)
    def __repr__(self):
        return 'Time: ' + str(self.time) + ' Loc: ' + str(self.loc) + ' Type: ' + str(self.type)

cases = []

def convert_time_str(time):
    [hours, minutes] = time.split(':')
    return int(hours)*60 + int(minutes)

while len(s) > 0:
    if s[0] == '':
        s = s[1:]
        continue

    T = int(s[0])
    [NA, NB] = s[1].split()
    NA = int(NA); NB = int(NB)
    leaving_A = s[2:NA+2]
    leaving_B = s[NA+2:NA+NB+2]

    timeline = []
    
    for trip in leaving_A:
        [leave_time, arrive_time] = trip.split()
        leave_time = convert_time_str(leave_time)
        arrive_time = convert_time_str(arrive_time)
        # create a 'ready' event when a train should be ok to reuse
        ready_time = arrive_time + T
        timeline.append(TrainEvent(leave_time, 'A', 'DEP'))
        timeline.append(TrainEvent(arrive_time, 'B', 'ARR'))
        timeline.append(TrainEvent(ready_time, 'B', 'RDY'))

    for trip in leaving_B:
        [leave_time, arrive_time] = trip.split()
        leave_time = convert_time_str(leave_time)
        arrive_time = convert_time_str(arrive_time)
        # create a 'ready' event when a train should be ok to reuse
        ready_time = arrive_time + T
        timeline.append(TrainEvent(leave_time, 'B', 'DEP'))
        timeline.append(TrainEvent(arrive_time, 'A', 'ARR'))
        timeline.append(TrainEvent(ready_time, 'A', 'RDY'))
    
    timeline.sort()
    cases.append(TrainTestCase(timeline))
    s = s[NA+NB+2:]
    
_counter = 0

for c in cases:
    _counter += 1
    train_count = {}
    train_count['A'] = 0
    train_count['B'] = 0

    timeline = c.timeline

    min_seen_A = INF
    min_seen_B = INF

    for event in timeline:
        type = event.type
        loc = event.loc
        time = event.time
        if event.type is 'RDY':
            train_count[loc] += 1
        elif event.type is 'ARR':
            pass # do nothing, the RDY is taken care of
        elif event.type is 'DEP':
            train_count[loc] -= 1
        
        min_seen_A = min(min_seen_A, train_count['A'])
        min_seen_B = min(min_seen_B, train_count['B'])
        
    print 'Case #%d: %d %d' % (_counter, -min_seen_A, -min_seen_B)
