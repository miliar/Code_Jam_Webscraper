import sys


class InputFileParser(object):
    def __init__(self, filename):
        self.test_cases = []
        with open(filename, 'r') as in_f:
            self.test_case_count = int(in_f.readline())
            for i in xrange(1, self.test_case_count + 1):
                tc = TestCase(i)
                tc.total, tc.r, tc.o, tc.y, tc.g, tc.b, tc.v = map(int, in_f.readline().strip().split(' '))
                self.test_cases.append(tc)


class TestCase(object):
    def __init__(self, index):
        self.index = index
        self.total = 0
        self.r = 0
        self.o = 0
        self.y = 0
        self.g = 0
        self.b = 0
        self.v = 0
        self.result = 0


def is_impossible(tc):
    colours = [tc.r, tc.o, tc.y, tc.g, tc.b, tc.v]
    colours.sort(reverse=True)
    return colours[0] > sum(colours[1:])


def get_first(colours):
    for colour, count in colours.items():
        if count > 0:
            colours[colour] = colours[colour] - 1
            return colour


def get_max_different(colour, colours):
    max_n = ''
    max_c = 0
    for name, count in colours.items():
        if name == colour:
            continue
        if count > max_c:
            max_n = name
            max_c = count
    colours[max_n] = colours[max_n] - 1
    return max_n


def place(tc):
    if is_impossible(tc):
        return 'IMPOSSIBLE'
    colours = {'R': tc.r, 'Y': tc.y, 'B': tc.b}
    ret = get_first(colours)
    for _i in xrange(tc.total - 1):
        ret += get_max_different(ret[-1], colours)
    return ret


if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit('input and output file not specified!')

    parser = InputFileParser(sys.argv[1])
    with open(sys.argv[2], 'w') as out_f:
        for tc in parser.test_cases:
            tc.result = place(tc)
            print 'Case #{0}: {1}'.format(tc.index, tc.result)
            out_f.write('Case #{0}: {1}\n'.format(tc.index, tc.result))
