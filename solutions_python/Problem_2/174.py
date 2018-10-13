
from collections import defaultdict


class time(int):
    def __new__(cls, h_or_str, m=None):
        if m is not None:
            return super(time, cls).__new__(cls, 60 * h_or_str + m)
        if isinstance(h_or_str, str):
            h, m = map(int, h_or_str.split(':'))
            return super(time, cls).__new__(cls, 60 * h + m)
        else:
            return super(time, cls).__new__(cls, h_or_str)

    @property
    def hour(self):
        return self // 60

    @property
    def minute(self):
        return self % 60

    def __repr__(self):
        return 'time(%r)' % str(self)

    def __str__(self):
        return '%02d:%02d' % (self.hour, self.minute)
        


class event(object):
    def __init__(self, time, place, kind):
        self.time = time
        self.place = place
        self.kind = kind

    def __str__(self):
        return '%s %s %s' % (self.time, self.kind, self.place)

    def __repr__(self):
        return 'event(%r, %r, %r)' % (self.time, self.place, self.kind)

    def __cmp__(self, other):
        # compare by time parameters, and use the kind as a tiebreaker
        # so ready events occur before depart events
        if self.time < other.time:
            return -1
        elif self.time > other.time:
            return 1
        else:
            if self.kind == 'ready':
                return -1
            elif self.kind == 'depart':
                return 1
            else:
                return 0


class trip(object):
    def __init__(self, origin, destination, depart, arrive):
        self.origin = origin
        self.destination = destination
        self.depart = time(depart)
        self.arrive = time(arrive)

    def __repr__(self):
        return 'trip(%r, %r, %r, %r)' % (self.origin, self.destination,
                                         self.depart, self.arrive)

    def events(self):
        return [event(self.depart, self.origin, 'depart'),
                event(self.arrive, self.destination, 'arrive')]


class case(object):
    def __init__(self, turn_time, schedule):
        self.turn_time= turn_time
        self.events = sum(map(trip.events, schedule), [])
        # change arrival events to ready events turn_time later
        for e in self.events:
            if e.kind == 'arrive':
                e.kind = 'ready'
                e.time = time(e.time + turn_time)
        self.events.sort()
                

    @staticmethod
    def readcase():
        T = input()
        NA, NB = map(int, raw_input().split())
        trips = []
        for origin, dest, num in ('A', 'B', NA), ('B', 'A', NB):
            for i in range(num):
                depart, arrive = raw_input().split()
                trips.append(trip(origin, dest, depart, arrive))
        return case(T, trips)

        

    def __repr__(self):
        return 'case(%d, %r)' % (self.turn_time, self.events)

    def __str__(self):
        return '\n'.join(map(str, self.events))

    def solution(self):
        start = {'A':0, 'B':0}
        curr = {'A':0, 'B':0}
        for e in self.events:
            if e.kind == 'depart':
                curr[e.place] -= 1
                if curr[e.place] < 0:
                    start[e.place] += 1
                    curr[e.place] += 1
            elif e.kind == 'ready':
                curr[e.place] += 1
        return (start['A'], start['B'])


# main code
input()  # skip number of cases line
CaseNo = 1
while True:
    try:
        c = case.readcase()
    except:
        break

    print 'Case #%d: %d %d' % ((CaseNo,) + c.solution())
    CaseNo += 1
