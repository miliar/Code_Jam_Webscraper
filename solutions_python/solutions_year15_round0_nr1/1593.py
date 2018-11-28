__author__ = 'msufa'

import sys


class InputFileParser(object):
    def __init__(self, filename):
        self.test_cases = []
        with open(filename, 'r') as in_f:
            self.test_case_count = int(in_f.readline())
            for i in xrange(1, self.test_case_count + 1):
                tc = TestCase(i)
                s_max_str, audience_str = in_f.readline().split(' ')
                tc.s_max = int(s_max_str)
                tc.audience = [int(person) for person in audience_str.strip()]
                self.test_cases.append(tc)


class TestCase(object):
    def __init__(self, index):
        self.index = index
        self.s_max = 0
        self.audience = []


if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit('input and output file not specified!')

    parser = InputFileParser(sys.argv[1])
    with open(sys.argv[2], 'w') as out_f:
        for tc in parser.test_cases:
            friends_needed = 0
            people_in_audience = 0
            for shyness in xrange(tc.s_max + 1):
                if (people_in_audience + friends_needed) < shyness:
                    friends_needed += shyness - (people_in_audience + friends_needed)
                people_in_audience += tc.audience[shyness]
            # print 'Case #{0}: {1}'.format(tc.index, friends_needed)
            out_f.write('Case #{0}: {1}\n'.format(tc.index, friends_needed))
