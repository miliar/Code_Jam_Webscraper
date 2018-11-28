"""
Created by bob on 11/04/15
"""

class Queue:
    """
    simple queue
    """

    def __init__(self):
        self.q = []
        self.l = 0

    def dequeue(self):
        if self.l:
            self.l -= 1
            return self.q.pop(0)
        return None

    def enqueue(self, x):
        self.l += 1
        self.q.append(x)

    def __len__(self):
        return self.l

class Reader:
    """
    base reader class
    """

    def __init__(self, filename):
        """
        reads the file and stores as a dictionary of testCases by reading the number of
        test cases and deriving the number of lines per test case . This number of lines
        is read for each test case which is then  stored as a list with each line being
        a string in that list
        """

        def lines_in_file():
            """
            returns the number of lines in the file excluding the first one
            """
            lines = 0
            for line in open(filename):
                lines += 1
            return lines - 1

        self.f = open(filename)
        self.number_test_cases = int(self.f.readline().strip())
        self.test_case_number = 0

    def test_cases(self, fixed_length=None):
        """
        generator to yield testcases
        """
        while self.test_case_number < self.number_test_cases:
            self.test_case_number += 1
            if fixed_length is None:
                descriptors = [int(x) for x in self.f.readline().strip().split(' ')]
            else:
                descriptors = [fixed_length]
            test_case = []
            for number_of_lines in descriptors:
                sub_test_case = []
                for idx in range(number_of_lines):
                    sub_test_case.append(self.f.readline().strip())
                test_case.append(sub_test_case)
            yield (self.test_case_number, test_case)


class Writer:
    """
    class to write the output in the format specified
    """

    def __init__(self, filename, output):
        self.number_cases = len(output)
        with open(filename, 'w') as f:
            for case, result in output.iteritems():
                f.write('Case #' + str(case) + ': ')
                for item in result:
                    f.write(str(item))
                f.write('\n')

    def get_number_cases(self):
        return (self.number_cases)

def solver(test):
    """
    solving algoritm for this problem. takes a test case as a list of lists, retruns a solution#
    as a list
    """
    def split(test, time, q):
        #print 'splitting', test
        highest = test[0]
        split_list = []
        x = 2
        while x <= highest / 2:
            split_list.append((x, highest - x))
            x += 1
        for a, b in split_list:
            _test = list(test)
            _test.pop(0)
            _test.append(a)
            _test.append(b)
            _test.sort(reverse = True)
            q.enqueue((tuple(_test), time + 1))
        #print 'getting', test
        return

    def eat(test):
        test = list(test)
        for i, plate in enumerate(test):
            test[i] = plate - 1
        test = [p for p in test if p]
        return tuple(test)

    solution = []
    time = 0
    test = test[0][1].split()
    test = [int(x) for x in test]
    test.sort(reverse = True)
    time = 0
    q = Queue()
    q.enqueue((tuple(test), time))

    mintime = 1000

    while len(q):
        test, time = q.dequeue()
        if time < mintime:
            if test[0] > 2:
                split(test, time, q)
            if test[0] > 1:
                q.enqueue((eat(test), time + 1))
            else:
                time += 1
                if mintime > time:
                    mintime = time

    solution.append(mintime)
    return solution







output = {}
in_filename = 'B-small-attempt13.in'
reader = Reader(in_filename)

for idx, test in reader.test_cases(2):
    result = solver(test)
    #result.append(test)
    output[idx] = result

out_filename = in_filename[:-2] + 'out'
writer = Writer(out_filename, output)
