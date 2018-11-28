#!/usr/bin/python

class Time(object):
    def __init__(self, text):
        self.hour, self.minute = tuple(int(x) for x in text.split(':'))
    def __cmp__(self, other):
        if not isinstance(other, Time):
            raise ValueError("%s is not a Time" % other)
        if self.hour == other.hour:
            if self.minute == other.minute:
                return 0
            elif self.minute < other.minute:
                return -1
            else:
                return 1
        elif self.hour < other.hour:
            return -1
        else:
            return 1
    def __add__(self, delta):
        hour, minute = self.hour, self.minute
        minute += delta
        while minute > 59:
            minute -= 60
            hour += 1

        return Time("%02d:%02d" % (hour, minute))
    def __repr__(self):
        return "%02d:%02d" % (self.hour, self.minute)

def cases(input):
    ncases = int(input.readline().strip())

    while ncases > 0:
        tat = int(input.readline().strip())
        na, nb = tuple(int(x) for x in input.readline().split())
        trips = []
        count = 0
        while count < na:
            tstart, tend = tuple(Time(x) for x in input.readline().split())
            trips.append((tstart, tend, 'ab'))
            count += 1
        count = 0
        while count < nb:
            tstart, tend = tuple(Time(x) for x in input.readline().split())
            trips.append((tstart, tend, 'ba'))
            count += 1
        yield (tat, trips)
        ncases -= 1

def simulate(turnaround, trips):
    ta, tb = 0, 0
    trainsAtA = []
    trainsAtB = []

    for tstart, tend, way in sorted(trips):
        # print tstart, tend, { 'ab': 'A -> B', 'ba': 'B -> A' }[way]
        if way == 'ab':
            tdest = trainsAtB
            if trainsAtA and trainsAtA[0] <= tstart:
                trainsAtA = trainsAtA[1:]
            else:
                ta += 1
        else:
            tdest = trainsAtA
            if trainsAtB and trainsAtB[0] <= tstart:
                trainsAtB = trainsAtB[1:]
            else:
                tb += 1
        tdest.append(tend + turnaround)
        tdest.sort()
        # print trainsAtA
        # print trainsAtB

    return ta, tb

if __name__ == '__main__':
    import sys

    for n, case in enumerate(cases(sys.stdin)):
        a, b = simulate(*case)
        print "Case #%d: %d %d" % (n + 1, a, b)
