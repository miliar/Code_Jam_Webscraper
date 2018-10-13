#!/usr/bin/python

import os
import sys

from cStringIO import StringIO
import unittest


def yield_line_of_items(reader):
    for x in reader.readline().strip().split():
        yield x

def read_line_of_items(reader):
    return list(yield_line_of_items(reader))

def yield_line_of_ints(reader):
    for i in yield_line_of_items(reader):
        yield int(i)

def read_line_of_ints(reader):
    return list(yield_line_of_ints(reader))

def yield_lines_of_items(reader, num=1):
    for i in range(num):
        yield read_line_of_items(reader)

def read_lines_of_items(reader, num=1):
    return list(yield_lines_of_ints(reader, num))

def yield_lines_of_ints(reader, num=1):
    for i in range(num):
        yield read_line_of_ints(reader)

def read_lines_of_ints(reader, num=1):
    return list(yield_lines_of_ints(reader, num))

class Snapper(object):
    def __init__(self, input):
        self.on = False
        self.input = input
    def has_power(self):
        return self.input.gives_power()
    def gives_power(self):
        return self.on and self.has_power()
    def toggle(self):
        self.on = not self.on

class Light(Snapper):
    def gives_power(self):
        return False

class Socket(Snapper):
    def __init__(self):
        self.on = True
    def gives_power(self):
        return True

class Solver(object):
    def __init__(self, input_name):
        self.input_name = input_name
        self.output_name = self._make_output_name()

    def _make_output_name(self):
        basename, ext = os.path.splitext(self.input_name)
        output_name = basename + ".out"
        return output_name

    def open_output(self):
        return open(self.output_name, "w")

    def open_input(self):
        return open(self.input_name, "r")

    def main(self):
        input = self.open_input()
        output = self.open_output()
        self.solve(input, output)
        input.close()
        output.close()

    def solve(self, input, output):
        number_of_cases = read_line_of_ints(input)[0]
        for casenr in xrange(number_of_cases):
            result = self.solve_case(*read_line_of_ints(input))
            output.write("Case #%d: %s\n" % (casenr+1, result))

    def solve_case(self, number_of_snappers, number_of_snaps):
        light = self.init_snappers(number_of_snappers)
        self.do_snaps(number_of_snaps)
        if light.has_power():
            return "ON"
        else:
            return "OFF"

    def init_snappers(self, number_of_snappers):
        self.snappers = list()
        previous = Socket()
        for i in xrange(number_of_snappers):
            snapper = Snapper(previous)
            self.snappers.append(snapper)
            previous = snapper
        return Light(previous)

    def do_snaps(self, number_of_snaps):
        for i in xrange(number_of_snaps):
            self.snap()

    def snap(self):
        toggle_list = list()
        for snapper in self.snappers:
            if snapper.has_power():
                toggle_list.append(snapper)
            else:
                break
        junk = [snapper.toggle() for snapper in toggle_list]

# === Verify correctness of sample data
class SampleTester(unittest.TestCase):
    def setUp(self):
        self.data = open("sample.correct", "r").read()
    def test_sample(self):
        output = StringIO()
        solver = Solver("sample.in")
        input = solver.open_input()
        solver.solve(input, output)
        self.assertEqual(self.data, output.getvalue())

if __name__ == "__main__":
    input_name = sys.argv[1]
    if input_name == "test":
        suite = unittest.TestLoader().loadTestsFromTestCase(SampleTester)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        import time
        start = time.time()
        solver = Solver(input_name)
        solver.main()
        end = time.time()
        print "Time spent: %s" % time.strftime("%M minutes, %S seconds", time.gmtime(end-start))
