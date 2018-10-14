import sys


class InputFileParser(object):
    def __init__(self, filename):
        self.test_cases = []
        with open(filename, 'r') as in_f:
            self.test_case_count = int(in_f.readline())
            for i in xrange(1, self.test_case_count + 1):
                tc = TestCase(i)
                tc.distance, horse_count = map(int, in_f.readline().strip().split(' '))
                for _j in xrange(horse_count):
                    position, speed = map(int, in_f.readline().strip().split(' '))
                    horse = Horse(position, speed)
                    horse.time_left = float(tc.distance - position) / float(speed)
                    tc.horses.append(horse)
                tc.horses.sort(key=lambda horse: horse.position)
                self.test_cases.append(tc)


class TestCase(object):
    def __init__(self, index):
        self.index = index
        self.distance = 0
        self.horses = []
        self.result = 0


class Horse(object):
    def __init__(self, position, speed):
        self.position = position
        self.speed = speed
        self.time_left = 0.0


def find_slowest(horses):
    return sorted(horses, key=lambda horse: horse.time_left, reverse=True)[0]


def calculate_speed(distance, horses):
    slowest_horse = find_slowest(horses)
    return float(distance) / slowest_horse.time_left


if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit('input and output file not specified!')

    parser = InputFileParser(sys.argv[1])
    with open(sys.argv[2], 'w') as out_f:
        for tc in parser.test_cases:
            tc.result = calculate_speed(tc.distance, tc.horses)
            print 'Case #{0}: {1:.6f}'.format(tc.index, tc.result)
            out_f.write('Case #{0}: {1:.6f}\n'.format(tc.index, tc.result))
