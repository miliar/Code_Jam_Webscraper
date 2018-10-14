"""
Some CodeJam base classes.

author: Martin Conte Mac Donell <Reflejo@gmail.com>
"""

import sys
from Queue import Empty
from optparse import OptionParser

_IN_FILE = 'input.in'

try:
    import psyco
    psyco.full()
except:
    pass

def parsein(fmt, pset):
    all = pset.split(' ')
    for i, f in enumerate(fmt.lower()):
        if f == 'i':
            all[i] = int(all[i])

        elif f == 'f':
            all[i] = float(all[i])


    return all

def _parse_options():
    parser = OptionParser()
    parser.add_option("-d", "--debug", dest="debug", 
                      action="store_true", default=False, 
                      help="Show debug information")
    parser.add_option("-w", "--workers", dest="workers", default="1",
                      type="int", help="Number of workers proccess")
    parser.add_option("-i", "--inputfile", dest="infile", default=_IN_FILE,
                      type="str", help="Input file path")
    (options, args) = parser.parse_args()
    return options

def _collect(fp):
    M = parsein('i', fp.readline())
    return M, []

def _scollect(fp, first):
    return []

class Solver(object):

    def __init__(self, debug, cache, first, collection): 
        self._debug = debug
        self._cache = cache
        self._first = first
        self._collection = collection

    def debug(self, msg):
        if self._debug:
            print msg


class Problem(object):
    
    def __init__(self, solver, cachefc=None):
        options = _parse_options()
        self._debug = options.debug
        self._infile = options.infile

        self._solver = solver
        self._cache = cachefc() if cachefc else None

        self._collection = []
        self._first = 0

    def _sets(self, init_collect, set_collect):
        # Read lines from input file and yield problem set
        file_pointer = open(self._infile)
        self._first, self._collection = init_collect(file_pointer)

        i = 0
        while True:
            i += 1
            line = file_pointer.readline().strip()
            if not line:
                # EOF
                break

            first = line.strip()
            if not first:
                break

            lines = [first]
            for line in set_collect(file_pointer, first):
                lines.append(line)

            yield lines

    def solve(self, set_collect=_scollect, init_collect=_collect):
        """
        Solve CodeJam input problem, reading lines from input file
        """
        fileout = open('%s.out' % self._infile, 'w')
        for i, set_ in enumerate(self._sets(init_collect, set_collect)):
            s = self._solver(self._debug, self._cache, self._first, 
                             self._collection)
            case = 'Case #%d: %s' % (i + 1, s.solve(set_))
            s.debug(case)
            fileout.write(case + '\n')

        fileout.close()
