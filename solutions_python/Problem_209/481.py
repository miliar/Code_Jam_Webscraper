import math

class Pancake:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.radius_ord = None
        self.height_ord = None

    @staticmethod
    def parse(line):
        [radius, height] = map(int, line.strip().split())
        return Pancake(radius, height)

    def __repr__(self):
        return "r(%d) h(%d) ro(%d) ho(%d)" % (self.radius, self.height, self.radius_ord, self.height_ord)

class TestCase:
    id = 1

    def __init__(self, pancakes, stack_size):
        self.pancakes = pancakes
        self.stack_size = stack_size

        TestCase.id += 1

    @staticmethod
    def parse(fh):
        pancake_count, stack_size = fh.readline().strip().split(' ')
        pancakes = [ Pancake.parse(fh.readline().strip()) for i in range(int(pancake_count)) ]
        return TestCase(pancakes, int(stack_size))

def parse():
    import sys
    fh = open(sys.argv[1])
    testcase_count = int(fh.readline())

    testcases = []
    for i in range(testcase_count):
        testcases.append(TestCase.parse(fh))

    return testcases

def calc_side_area(pancake):
    return pancake.height * pancake.radius * 2 * math.pi

def calc_flat_area(pancake):
    return (pancake.radius ** 2) * math.pi

def calc_test_case(testcase):
    testcase.pancakes.sort(key=lambda pancake: (pancake.radius, pancake.height))
    testcase.pancakes.reverse()
    for i in range(len(testcase.pancakes)):
        testcase.pancakes[i].radius_ord = i

    areas = [ (calc_side_area(pancake), pancake) for pancake in testcase.pancakes ]
    areas.sort()
    areas.reverse()
    for i in range(len(testcase.pancakes)):
        areas[i][1].height_ord = i

    starters_count = len(testcase.pancakes) - testcase.stack_size + 1

    max_area = []
    for pancake in testcase.pancakes[:starters_count]:
        max_area.append(calc_flat_area(pancake) + calc_side_area(pancake) + sum(map(lambda area: calc_side_area(area[1]), filter(lambda area: area[1].radius_ord > pancake.radius_ord, areas)[:testcase.stack_size - 1])))

    return max(max_area)

def main():
    testcases = parse()
    i = 1
    for testcase in testcases:
        print "Case #%d: %.9f" % (i, calc_test_case(testcase))
        i += 1

if __name__ == '__main__':
    main()
