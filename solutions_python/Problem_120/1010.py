#!/usr/bin/env python
# encoding: utf-8

import sys
from math import pi


class memoize:
    """Decorator class for memoization of a recursive function"""
    def __init__(self, function):
        self.function = function
        self.memoized = {}

    def __call__(self, *args):
        try:
            return self.memoized[args]
        except KeyError:
            self.memoized[args] = self.function(*args)
            return self.memoized[args]


def main():
    """Read in the specified file and print out the expected output."""
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print 'usage: ./Bullseye.py file'
        sys.exit(1)
    with open(filename, 'rU') as file_handle:
        casenum = int(file_handle.readline())
        for case in range(1, casenum + 1):
        #for case in range(1, 3):
            print handle_case(case, [file_handle.readline()])


def handle_case(case, lines, **args):
    """Return a string containing the expected output given a single case.

    Handles the case supplied through the given case and lines and returns a
    string containing the expected output of the given input. The **args may be
    used to contain any additional input variables that may have been
    preprocessed.

    Args:
        case: Number specifying the current case number
        lines: List of input lines relevant to the case
        **args: Additional arguments (e.g. preprocessed input)

    Returns:
        A string of the expected output of the corresponding test case.
    """

    r, t = [int(x) for x in lines[0].split()]
    numrings = 0
    newr = newring_radius(r)
    # newr is the starting point
    # always subtract by 4
    while t > 0:
        t = t - (newr) # lose 1 milliliter of paint
        r = r + 2 # bigger last radius
        if t >= 0: # she managed to finish the ring with paint left
            numrings = numrings + 1 # draw the rings
            oldr = newr
            newr = newr + 4
    result = '%d' % numrings
    return 'Case #%d: %s' % (case, result)


def area_of_ring(lastr):
    """Return the area of the new black ring given the radius of the last ring"""
    r1 = lastr**2
    r2 = (r1 + 1)**2
    area = pi*(r2 - r1)
    return area


@memoize
def newring_radius(lastr):
    r1 = lastr**2
    r2 = (lastr + 1)**2
    newr = (r2 - r1)
    return newr


if __name__ == '__main__':
    main()
