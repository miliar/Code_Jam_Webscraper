#!/usr/bin/python

class Series(object):

    def __init__(self, numbers):
        self.nb_googlers = numbers[0]
        self.nb_surprises = numbers[1]
        self.min_best_result = numbers[2]
        self.points = numbers[3:]

    def max_googlers(self):
        if self.min_best_result <= 0:
            return self.nb_googlers

        # All higher than (min_best_result * 3) - 2 are good and not surprising (3 4 4)
        remaining_points = [x for x in self.points if x < ((self.min_best_result * 3) - 2)]
        nb_googlers = len(self.points) - len(remaining_points)

        remaining_points.sort()
        i = 0
        while i<self.nb_surprises and len(remaining_points):
            total = remaining_points.pop()
            if total > 0 and total >= ((self.min_best_result * 3) - 4):
                nb_googlers += 1
            i += 1
        return nb_googlers

def max(numbers):
    return numbers

with open('B-large.in') as f:
    nb_tests = int(f.readline())
    i = 1
    for line in f.readlines():
        series = Series([int(x) for x in line.split(" ")])
        print "Case #%d: %d" % (i, series.max_googlers())
        i += 1

