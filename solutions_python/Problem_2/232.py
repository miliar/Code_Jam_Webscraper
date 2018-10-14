#!/usr/bin/env python
"train timetable"
import sys



class Event(dict):
    "Event"
    LOC_A, LOC_B = "A", "B"
    TYP_DEP, TYP_ARR = '1departure', '0arrival'

    def __init__(self, time, orig, type, turnaround):
        super(Event, self).__init__()
        self['time'] = self.parse_time(time)
        if type == Event.TYP_ARR:
            self['time'] += turnaround
        self['orig'] = orig
        self['dest'] = self.other_location(orig)
        self['type'] = type
    def other_location(self, loc):
        if loc == Event.LOC_A:
            return Event.LOC_B
        return Event.LOC_A
    def parse_time(self, time):
        hours, mins = time.strip().split(':')
        hours, mins = int(hours), int(mins)
        return hours * 60 + mins
    @staticmethod
    def cmp(ev_a, ev_b):
        if ev_a['time'] == ev_b['time']:
            return cmp(ev_a['type'], ev_b['type'])
        return cmp(ev_a['time'], ev_b['time'])


def read_input(finp):
    N = int(finp.readline())
    for n in xrange(N):
        T = int(finp.readline())
        NA, NB = finp.readline().strip().split()
        NA, NB = int(NA), int(NB)
        events = []
        for na in xrange(NA):
            departure, arrival = finp.readline().strip().split()
            events.append(Event(departure, Event.LOC_A, Event.TYP_DEP, T))
            events.append(Event(arrival, Event.LOC_A, Event.TYP_ARR, T))
        for nb in xrange(NB):
            departure, arrival = finp.readline().strip().split()
            events.append(Event(departure, Event.LOC_B, Event.TYP_DEP, T))
            events.append(Event(arrival, Event.LOC_B, Event.TYP_ARR, T))
        if False: print n, na, nb
        events.sort(cmp=Event.cmp)

        #from com.moveki import progbase
        #progbase.yaml_dump('-', events)
        needed_in = {
                Event.LOC_A : 0,
                Event.LOC_B : 0,
                }
        max_needed_in = {
                Event.LOC_A : 0,
                Event.LOC_B : 0,
                }
        for e in events:
            if e['type'] == Event.TYP_ARR:
                needed_in[e['dest']] -= 1
            elif e['type'] == Event.TYP_DEP:
                needed_in[e['orig']] += 1
                if needed_in[e['orig']] > max_needed_in[e['orig']]:
                    max_needed_in[e['orig']] = needed_in[e['orig']]

                #print "-------------"
                #progbase.yaml_dump('-', e)
                #progbase.yaml_dump('-', needed_in)
            else:
                raise RuntimeError("oops")
        max_needed_in['ncase'] = n + 1
        print "Case #%(ncase)d: %(A)d %(B)d" % (max_needed_in)
        #progbase.yaml_dump('-', max_needed_in)





def main():
    read_input(sys.stdin)


if __name__ == "__main__":
    main()
