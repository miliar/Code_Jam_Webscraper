class TestCase:
    id = 1

    def __init__(self, data, size):
        self.data = data
        self.size = size

        TestCase.id += 1

    @staticmethod
    def parse(line):
        pancakes, size = line.split(' ')
        return TestCase(pancakes, int(size))

def parse():
    import sys
    fh = open(sys.argv[1])
    testcase_count = int(fh.readline())

    testcases = []
    for i in range(testcase_count):
        testcases.append(TestCase.parse(fh.readline()))

    return testcases

def reduce_by_one(active):
    return map(lambda x: x - 1, active)

def flip(pancake):
    return '+' if '-' == pancake else '-'

def calculate(testcase):
    active = []
    count = 0

    for pancake in testcase.data:
        current = pancake if len(active) % 2 == 0 else flip(pancake)

        if current == '-':
            active.append(testcase.size)

        active = reduce_by_one(active)
        if len(active) > 0 and active[0] == 0:
            count += 1
            active = active[1:]

    return count if len(active) == 0 else "IMPOSSIBLE"

def main():
    testcases = parse()
    i = 1
    for testcase in testcases:
        print "Case #%d: %s" % (i, calculate(testcase))
        i += 1

if __name__ == '__main__':
    main()
