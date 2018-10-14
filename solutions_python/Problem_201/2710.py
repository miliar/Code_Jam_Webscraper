import sys
import copy


class InputFileParser(object):
    def __init__(self, filename):
        self.test_cases = []
        with open(filename, 'r') as in_f:
            self.test_case_count = int(in_f.readline())
            for i in xrange(1, self.test_case_count + 1):
                tc = TestCase(i)
                tc.stalls, tc.people = [int(val) for val in in_f.readline().strip().split(' ')]
                self.test_cases.append(tc)


class TestCase(object):
    def __init__(self, index):
        self.index = index
        self.stalls = 0
        self.people = 0
        self.rmax = 0
        self.rmin = 0


def void_size(void):
    return void[1] - void[0]


def larger_void(first, second):
    return first if void_size(first) >= void_size(second) else second


def stall_occupied(stall, layout):
    return layout[stall] > 0


def find_largest_void(layout):
    # we assume that the 1st stall is always occupied
    largest = [0, 0]
    current = [0, 0]
    in_void = False
    for stall in xrange(len(layout)):
        if in_void and stall_occupied(stall, layout):
            in_void = False
            current[1] = stall
            largest = copy.copy(larger_void(largest, current))
        if not in_void and not stall_occupied(stall, layout):
            in_void = True
            current[0] = stall
    return largest


def preferred_stall(void):
    vs = void_size(void)
    distance_from_beginning = (vs / 2) + (vs % 2) - 1
    return (void[0] + distance_from_beginning), (vs - distance_from_beginning - 1), distance_from_beginning


def place_person(layout):
    largest_void = find_largest_void(layout)
    ps, rmax, rmin = preferred_stall(largest_void)
    updated_layout = copy.copy(layout)
    updated_layout[ps] = 1
    return updated_layout, rmax, rmin


def place_people(stalls, people):
    layout = [0 for _i in xrange(stalls + 2)]
    # guards
    layout[0] = 1
    layout[-1] = 1
    rmax = 0
    rmin = 0
    for _i in xrange(people):
        layout, rmax, rmin = place_person(layout)
    return rmax, rmin


if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit('input and output file not specified!')

    parser = InputFileParser(sys.argv[1])
    with open(sys.argv[2], 'w') as out_f:
        for tc in parser.test_cases:
            tc.rmax, tc.rmin = place_people(tc.stalls, tc.people)
            print 'Case #{0}: {1} {2}'.format(tc.index, tc.rmax, tc.rmin)
            out_f.write('Case #{0}: {1} {2}\n'.format(tc.index, tc.rmax, tc.rmin))
