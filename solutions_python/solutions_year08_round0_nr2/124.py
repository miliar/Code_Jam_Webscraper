#!/usr/bin/env python
"""Google Code Jam qualification round, 2. By Hraban Luyat.

See http://google.com/codejam/ for more info.

"""
import datetime
import sys
import time

USAGE = """
Usage:

    ./gcj2 -O INPUT_FILENAME

"""

# Event types. Value of the defines matters: lower takes precedence in event
# queue.
EV_TRAIN_ARRIV = 0
EV_TRAIN_LEAVE = 1

class Event(object):
    """Event slot in a discrete event simulation.

    If trains arrive and leave at the same time, the arriving trains take
    precedence. Instances of this class are not aware of turnaround times, so a
    train that arrives can immediately leave.

    """
    def __init__(self, time, type):
        assert(isinstance(time, datetime.timedelta))
        assert(type in (EV_TRAIN_LEAVE, EV_TRAIN_ARRIV))
        self.time = time
        self.type = type
    def __cmp__(self, x):
        return cmp(self.time, x.time) or cmp(self.type, x.type)

class Station(object):
    """Discrete event simulation of a train station.

    The station has an internal counter of the number of available trains.
    When a train arrives that counter is increased by one.  Whenever a train
    has to leave the station and that counter is higher than zero, it is
    reduced by one. If it is zero, stock is bought from an endless pool. At the
    end of the simulation the number of times stock has been bought indicates
    the number of trains needed in stock initially to not have to buy any stock
    on the fly.

    There is also a list of events that is built up by calling the add_event()
    method. Once all events for this station have been added the simulate()
    method is called, which returns the number of trains the station should
    start with. Only call simulate() once!

    Lastly, there is the turnaround time. It indicates how long a train has to
    be stored at the station after a arrival before it can leave again. This is
    implemented by delaying all arriving trains by that many minutes.

    """

    def __init__(self, turnaround):
        """The turnaround argument is in minutes."""
        self._ta = datetime.timedelta(minutes=turnaround)
        self._events = []
        self._stock = 0
        self._stock_bought = 0

    def _train_arriv(self):
        self._stock += 1

    def _train_leave(self):
        if self._stock:
            self._stock -= 1
        else:
            self._stock_bought += 1

    def add_event(self, ev):
        assert(isinstance(ev, Event))
        if ev.type == EV_TRAIN_ARRIV:
            ev.time += self._ta
        self._events.append(ev)

    def simulate(self):
        self._events.sort()
        for ev in self._events:
            self._handlers[ev.type](self)
        return self._stock_bought

    _handlers = {
            EV_TRAIN_ARRIV: _train_arriv,
            EV_TRAIN_LEAVE: _train_leave,
            }

def _parse_table_time(line):
    """Parse a row from the timetable to two events."""
    # Time tuples for leave and join times.
    t_l, t_a = (time.strptime(e, "%H:%M") for e in line.strip().split())
    # datetime.timedelta objects.
    t_l = datetime.timedelta(hours=t_l[3], minutes=t_l[4])
    t_a = datetime.timedelta(hours=t_a[3], minutes=t_a[4])
    return (Event(t_l, EV_TRAIN_LEAVE), Event(t_a, EV_TRAIN_ARRIV))

def gcj2(path):
    f = open(path, "r")
    n = int(f.readline().strip())
    for i in xrange(1, n + 1):
        t = int(f.readline().strip())
        stn_a = Station(t)
        stn_b = Station(t)
        na, nb = (int(j) for j in f.readline().strip().split())
        # A -> B
        for j in xrange(na):
            ev_leave, ev_arriv = _parse_table_time(f.readline())
            stn_a.add_event(ev_leave)
            # Trains leaving from A arrive at B.
            stn_b.add_event(ev_arriv)
        # B -> A
        for j in xrange(nb):
            ev_leave, ev_arriv = _parse_table_time(f.readline())
            stn_b.add_event(ev_leave)
            stn_a.add_event(ev_arriv)
        print "Case #%d: %d %d" % (i, stn_a.simulate(), stn_b.simulate())

def main():
    #print __doc__
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        #sys.exit(USAGE)
        print >> sys.stderr, USAGE
        sys.exit(1)
    gcj2(sys.argv[1])

if __name__ == "__main__":
    main()
