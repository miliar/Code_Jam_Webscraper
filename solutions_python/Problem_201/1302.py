import math

class TestCase:
    id = 1

    def __init__(self, stall_count, people_count):
        self.stall_count = stall_count
        self.people_count = people_count

        TestCase.id += 1

    @staticmethod
    def parse(line):
        [stall_count, people_count] = map(int, line.split(' '))
        return TestCase(stall_count, people_count)

def parse():
    import sys
    fh = open(sys.argv[1])
    testcase_count = int(fh.readline())

    testcases = []
    for i in range(testcase_count):
        testcases.append(TestCase.parse(fh.readline()))

    return testcases

def partition(partitions):
    next_partitions = []
    for partition in partitions:
        next_partitions.append(partition / 2)
        next_partitions.append((partition - 1) / 2)
    return next_partitions

def get_max_partition_after(number, partition_count):
    partitions = [number]
    while partition_count >= len(partitions):
        partition_count -= len(partitions)
        partitions = filter(lambda x: x != 0, partition(partitions))
    partitions.sort()
    partitions.reverse()
    return partitions[partition_count]

def get_max_min_from_partition(partition):
    return partition / 2, (partition - 1) / 2

def calculate(testcase):
    max_partition_before = get_max_partition_after(testcase.stall_count, testcase.people_count - 1)
    return get_max_min_from_partition(max_partition_before)

def main():
    testcases = parse()
    i = 1
    for testcase in testcases:
        max_value, min_value = calculate(testcase)
        print "Case #%d: %d %d" % (i, max_value, min_value)
        i += 1

if __name__ == '__main__':
    main()
