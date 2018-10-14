#!/usr/bin/env python

import sys

class PlanItem:
    def __init__(self, station, times):
        items = times.split(' ')
        start = items[0].split(':')
        end = items[1].split(':')

        self.station = station
        self.start_time = int(start[0]) * 60 + int(start[1])
        self.end_time = int(end[0]) * 60 + int(end[1])

    def __cmp__(self, other):
        if self.start_time <> other.start_time:
            return self.start_time - other.start_time
        else:
            return self.end_time - other.end_time

    def __repr__(self):
        return '%s %d - %d' % (self.station, self.start_time, self.end_time)

class TimeTable:
    def __init__(self, turnaround_time):
        self.turnaround_time = turnaround_time
        self.items = []
        self.train_count = {'A': 0, 'B': 0}

    def add(self, item):
        self.items.append(item)
        self.items.sort()

    def process(self):
        while len(self.items):
            item = self.items.pop(0)
            current_station = item.station
            self.train_count[current_station] += 1

            start_time = item.end_time + self.turnaround_time
            while True:
                next = None
                for i in xrange(len(self.items)):
                    it = self.items[i]
                    if it.station <> current_station and it.start_time >= start_time:
                        next = self.items.pop(i)
                        break

                if not next:
                    break

                current_station = next.station
                start_time = next.end_time + self.turnaround_time

        return self.train_count

def main():
    if len(sys.argv) == 1:
        f = open('test.in')
    else:
        f = open(sys.argv[1])

    count = int(f.readline())
    for i in xrange(1, count + 1):

        turnaround_time = int(f.readline().strip())
        time_table = TimeTable(turnaround_time)

        counts = f.readline().strip().split(' ')
        NA = int(counts[0])
        NB = int(counts[1])

        for n in xrange(NA):
            line = f.readline().strip()
            time_table.add(PlanItem('A', line))

        for n in xrange(NB):
            line = f.readline().strip()
            time_table.add(PlanItem('B', line))

        counts = time_table.process()

        print 'Case #%d: %d %d' % (i, counts['A'], counts['B'])

if __name__ == '__main__':
    main()
