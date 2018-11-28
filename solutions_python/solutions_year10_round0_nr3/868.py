import sys
import unittest
from collections import deque

def run(runs, capacity, groups):
    money = 0
    for _ in range(0, runs):
        boarded = []
        for group in groups:
            if fits(group, capacity, boarded):
                money += group
                boarded.append(group)
            else:
                break;

        for _ in boarded:
            groups.append(groups.popleft())

    return money

def fits(group, capacity, boarded):
    if not boarded:
        boarded = [0]
        
    on_board = reduce(lambda x, y: x + y, boarded)
    return on_board + group <= capacity

def make_tuple_lines(lines):
  for i in range(0, len(lines), 2):
    line = lines[i: i + 2]
    if len(line) == 2:
      yield tuple(line)

if __name__ == '__main__':
    if not sys.argv[1:]:
        print "call me with the .in file, please"
        sys.exit()

    file = open(sys.argv[1])
    lines = map(lambda x: x.rstrip(), file.readlines())
    for (offset, line) in enumerate(list(make_tuple_lines(lines[1:]))):
        header = tuple(line[0].split())
        runs = int(header[0])
        capacity = int(header[1])
        groups = deque([int(p) for p in line[1].split(' ')])
        print "Case #%i: %i" % (offset + 1, run(runs=runs, capacity=capacity,groups=groups))

#
# Tests
#
class ThemeParkTest(unittest.TestCase):
    def test_first_case(self):
        self.assertEquals(21, run(runs=4, capacity=6, groups=deque([1, 4, 2, 1])))

    def test_second_case(self):
        self.assertEquals(100, run(runs=100, capacity=10, groups=deque([1])))

    def test_third_case(self):
        self.assertEquals(20, run(runs=5, capacity=5, groups=deque([2,4,2,3,4,2,1,2,1,3])))

    def test_rollover_case(self):
        self.assertEquals(30, run(runs=2, capacity=100, groups=deque([5, 5, 5])))
        

        
class CapacityTest(unittest.TestCase):
    def test_it_fits(self):
        self.assertTrue(fits(boarded=[1], group=2, capacity=4))

    def test_it_fits_and_they_are_full(self):
        self.assertTrue(fits(boarded=[1,4], group=1, capacity=6))

    def test_it_does_not_fit(self):
        self.assertFalse(fits(boarded=[1,4], group=10, capacity=6))

