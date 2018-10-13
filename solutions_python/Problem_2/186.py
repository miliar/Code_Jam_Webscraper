#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys

class Solution:
    def main(self, filename):
        self.dataset_stream = open(filename, 'r')
        line = self.dataset_stream.readline()
        self.cases_left = int(line)
        print "File contains %d testcases." % (self.cases_left)

        self.caseno = 1
        while self.cases_left > 0:
            self.cases_left -= 1
            self.readcase()
            self.printcase()
            self.solve()
            self.printsolution()
            self.caseno += 1

    def printsolution(self):
        print >> sys.stderr, "Case #%d: %d %d" % (self.caseno, self.spawn_a, self.spawn_b)

    def readcase(self):
        self.turnaround = int(self.dataset_stream.readline())
        line = self.dataset_stream.readline()
        tmp = line.split()
        trips_a = int(tmp[0])
        trips_b = int(tmp[1])
        self.timetable_a = []
        self.timetable_b = []
        for i in range(0, trips_a):
            line = self.dataset_stream.readline().strip().split()
            start = self.time_to_minutes(line[0])
            end = self.time_to_minutes(line[1])
            self.timetable_a.append([start, end])
        for i in range(0, trips_b):
            line = self.dataset_stream.readline().strip().split()
            start = self.time_to_minutes(line[0])
            end = self.time_to_minutes(line[1])
            self.timetable_b.append([start, end])

        self.timetable_a.sort(lambda x, y: cmp(x[0], y[0]))
        self.timetable_b.sort(lambda x, y: cmp(x[0], y[0]))

    def printcase(self):
        print "======================================"
        print "Turnaround time: %d" % self.turnaround
        print "Trips from A to B: %d" % len(self.timetable_a)
        for trip in self.timetable_a:
            print "    %s -> %s" % (self.minutes_to_time(trip[0]),
                                    self.minutes_to_time(trip[1]))
        print "Trips from B to A: %d" % len(self.timetable_b)
        for trip in self.timetable_b:
            print "    %s -> %s" % (self.minutes_to_time(trip[0]),
                                    self.minutes_to_time(trip[1]))

    def time_to_minutes(self, time):
        hh, mm = time.split(':')
        return int(hh)*60+int(mm)

    def minutes_to_time(self, minutes):
        return "%02d:%02d" % (int(minutes / 60), minutes % 60)

    def solve(self):
        ptr_a = 0
        ptr_b = 0
        trains_a = 0
        trains_b = 0
        spawn_a = 0
        spawn_b = 0
        running_a = []
        running_b = []
        for i in range(0, 24*60):
            if len(running_a) > 0:
                row_a = running_a[0]
                while row_a[1] == i:
                    print "Train arrived at A and turned around at %s" % self.minutes_to_time(i)
                    trains_b += 1
                    del running_a[0]
                    if len(running_a) > 0:
                        row_a = running_a[0]
                    else:
                        break

            if len(running_b) > 0:
                row_b = running_b[0]
                while row_b[1] == i:
                    print "Train arrived at B and turned around at %s" % self.minutes_to_time(i)
                    trains_a += 1
                    del running_b[0]
                    if len(running_b) > 0:
                        row_b = running_b[0]
                    else:
                        break

            if len(self.timetable_a) > 0:
                row_a = self.timetable_a[0]
                while row_a[0] == i:
                    del self.timetable_a[0]
                    if trains_a == 0:
                        print "Adding more trains to A"
                        spawn_a += 1
                    else:
                        trains_a -= 1
                    print "Train started at A at %s" % self.minutes_to_time(row_a[0])
                    row_a[1] += self.turnaround
                    running_a.append(row_a)
                    running_a.sort(lambda x, y: cmp(x[1], y[1]))

                    if len(self.timetable_a) > 0:
                        row_a = self.timetable_a[0]
                    else:
                        break

            if len(self.timetable_b) > 0:
                row_b = self.timetable_b[0]
                while row_b[0] == i:
                    del self.timetable_b[0]
                    if trains_b == 0:
                        print "Adding more trains to B"
                        spawn_b += 1
                    else:
                        trains_b -= 1
                    print "Train started at B at %s" % self.minutes_to_time(row_b[0])
                    row_b[1] += self.turnaround
                    running_b.append(row_b)
                    running_b.sort(lambda x, y: cmp(x[1], y[1]))

                    if len(self.timetable_b) > 0:
                        row_b = self.timetable_b[0]
                    else:
                        break
        self.spawn_a = spawn_a
        self.spawn_b = spawn_b

if __name__ == '__main__':
    filename = sys.argv[1]
    s = Solution()
    s.main(filename)
