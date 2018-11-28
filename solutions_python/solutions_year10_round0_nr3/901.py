import itertools
import sys

class TestCase(object):
    def __init__(self):
        self.id = 0
        self.R = 0
        self.k = 0
        self.N = []

    def solve(self):
        money = 0

        for i in range(0, self.R):
            ride = []

            while sum(ride) <= self.k and len(self.N) != 0:
                ride.append(self.N.pop())

            if sum(ride) > self.k:
                self.N.append(ride.pop())

            for n in ride:
                self.N.insert(0, n)

            money += sum(ride)

        print 'Case #%s: %s' % (self.id, money)


def read_input(filename):
    f = open(filename)

    ids = itertools.count(1)
    n_tests = None
    test_cases = []
    test_case = None

    for line in f:
        if n_tests == None:
            n_tests = int(line)
        elif test_case == None:
            test_case = TestCase()
            test_case.id = ids.next()

            parts = line.split(' ')
            test_case.R = int(parts[0])
            test_case.k = int(parts[1])
        else:
            test_case.N = list(reversed([int(n) for n in line.split(' ')]))
            test_cases.append(test_case)
            test_case = None

    return test_cases

def main():
    for t in read_input(sys.argv[1]):
        t.solve()

if __name__ == '__main__':
    sys.exit(main())
