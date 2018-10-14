"""Google Code Jam - Qualifying round - Problem B.

This is problem A of Google's 2014 Code Jam qualifying round.
"""
import sys
import getopt
import logging

logging.basicConfig(level=logging.ERROR)


class TestCase:

    def __init__(self, data):
        self.data=data
        self.cost = 0.0     # cost for farm
        self.farm = 0.0     # number of cookies per second from farm
        self.constant = 2.0 # start getting 2 cookies per second regardless
        self.x = 999999999  # target number of cookies to win
        logging.debug('TestCase.__init__: Got data=%s' % data)
        self.parse()

    def parse(self):
        values = self.data[0].strip().split()
        self.cost = float(values[0])
        self.farm = float(values[1])
        self.x = float(values[2])

    def cps(self, purchases):
        return self.constant + self.farm * len(purchases)

    def time_x(self, purchases):
        return self.x / self.cps(purchases)

    def time_farm(self, purchases):
        return self.cost / self.cps(purchases)

    def solve(self):
        purchaces = []
        while True:
            logging.debug('TestCase.solve: purchaces=%s' % purchaces)
            t_target = self.time_x(purchaces)
            logging.debug('TestCase.solve: t_target=%s' % t_target)
            t_farm = self.time_farm(purchaces)
            logging.debug('TestCase.solve: t_farm=%s' % t_farm)
            t_sofar = sum(purchaces)
            logging.debug('TestCase.solve: t_sofar=%s' % t_sofar)
            next_purchaces = [t_farm,] + purchaces
            t_n_sofar = sum(purchaces)
            t_n_target = self.time_x(next_purchaces)
            if t_sofar+t_target < t_farm+t_n_sofar+t_n_target:
                return t_target+t_sofar
            else:
                purchaces.append(t_farm)

class Datasets:

    testcases = []

    def __init__(self, numtests, data, numlines, tcclass):
        for i in range(numtests):
            testcase_data = data[:numlines]
            tc = tcclass(testcase_data)
            self.testcases.append(tc)
            data = data[numlines:]

    def solve_all(self):
        i = 1
        for test in self.testcases:
            result = test.solve()
            print "Case #%d: %s" % (i, result)
            i+=1


def processData(filename, numlines, case):
    with open(filename, 'r') as f:
        numtests = int(f.readline())
        test_cases_data = f.readlines()
        f.close()
        datasets = Datasets(numtests, test_cases_data, numlines, case)

    return datasets


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(sys.argv[1:], 'h', ['help'])
        except getopt.error, msg:
            raise Usage(msg)
        for o, a in opts:
            if o in ('-h', '--help'):
                print __doc__
                sys.exit(0)
        for arg in args:
            dataset = processData(arg, 1, TestCase)
            dataset.solve_all()
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2


if __name__ == '__main__':
    sys.exit(main())
