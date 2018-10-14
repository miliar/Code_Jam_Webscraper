from itertools import imap
import datetime


def stamp(self, kind, station, time):
    self.station = station
    h, m = map(int, time.split(':'))
    self.time = datetime.datetime(2000, 1, 1, hour=h, minute=m)
    self.__cmp__ = (lambda other: cmp(self.time, other.time))
    self.__str__ = (lambda: "%s: time(%s) station(%s)" % (kind, self.time, self.station))


class Arrival:
    def __init__(self, station, time):
        stamp(self, "Arrival", station, time)


class Departure:
    def __init__(self, station, time):
        stamp(self, "Departure", station, time)


def cmp_actions(a, b):
    if a == b:
        x = 0 if isinstance(a, Arrival) else 1
        y = 0 if isinstance(b, Arrival) else 1
        return cmp(x, y)
    return cmp(a, b)


class Train:
    def __init__(self, time=None):
        self.time = time
        self.__cmp__ = (lambda other: cmp(self.time, other.time))


class Station:

    def __init__(self, delay, count):
        self.delay = delay
        self.trains = [Train(None) for i in xrange(count)]

    def depart(self, time):
        train = None
        for t in self.trains:
            if t.time is None:
                train = t
                break
        if train is None:
            for t in self.trains:
                if t.time + self.delay <= time:
                    train = t
                    break
        try:
            self.trains.remove(train)
            return True
        except:
            return False

    def arrive(self, time):
        self.trains.append(Train(time))


def solve(delay, a, b, actions):
    a_start, b_start = 0, 0
    while True:
        a_station = Station(delay, a_start)
        b_station = Station(delay, b_start)
        ok = True
        for action in actions:
#            print action
            if isinstance(action, Departure):
                if action.station == 'a':
                    if not a_station.depart(action.time):
                        a_start += 1
                        ok = False
                        break
                else:
                    if not b_station.depart(action.time):
                        b_start += 1
                        ok = False
                        break
            else:
                if action.station == 'a':
                    a_station.arrive(action.time)
                else:
                    b_station.arrive(action.time)
        if ok:
            break
    return "%s %s" % (a_start, b_start)


a, b = 0, 0
n = int(raw_input())
for case in xrange(n):
    delay = datetime.timedelta(minutes=int(raw_input()))
    na, nb = map(int, raw_input().split())

    actions = []
    for i in xrange(na):
        depart, arrive = raw_input().split()
        actions.append(Departure('a', depart))
        actions.append(Arrival('b', arrive))

    for i in xrange(nb):
        depart, arrive = raw_input().split()
        actions.append(Departure('b', depart))
        actions.append(Arrival('a', arrive))

    print "Case #%i: %s" % (case + 1, solve(delay, na, nb, sorted(actions, cmp_actions)))

