"""Google Code Jam - Qualifying round - Problem A.

This is problem A of Google's 2010 Code Jam qualifying round.
"""
import sys
import getopt
import logging

logging.basicConfig(level=logging.ERROR)

class TestCase:

    def __init__(self, data):
        self.data=data
        self.answer1 = -1
        self.answer2 = -1
        self.rows1 = []
        self.rows2 = []
        logging.debug('TestCase.__init__: Got data=%s' % data)
        self.parse()

    def parse(self):
        self.answer1 = int(self.data[:1][0].strip())
        logging.debug('TestCase.parse: answer1=%s' % self.answer1)
        self.data=self.data[1:]
        for n in range(0,4):
            self.rows1.append([int(x) for x in self.data[n:n+1][0].split()])
        logging.debug('TestCase.parse: rows1=%s' % self.rows1)
        self.data = self.data[4:]
        self.answer2 = int(self.data[:1][0].strip())
        logging.debug('TestCase.parse: answer2=%s' % self.answer2)
        self.data=self.data[1:]
        for n in range(0,4):
            self.rows2.append([int(x) for x in self.data[n:n+1][0].split()])
        logging.debug('TestCase.parse: rows2=%s' % self.rows2)

    def solve(self):
        row1 = set(self.rows1[self.answer1-1])
        row2 = set(self.rows2[self.answer2-1])
        intersection = row1.intersection(row2)
        if len(intersection)==1:
            return intersection.pop()
        if len(intersection)==0:
            return "Volunteer cheated!"
        else:
            return "Bad magician!"

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


def processData(filename, numtests, numlines, case):
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
            dataset = processData(arg, 3, 10, TestCase)
            dataset.solve_all()
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2


if __name__ == '__main__':
    sys.exit(main())
