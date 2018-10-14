from itertools import islice
from collections import namedtuple
from sys import stdin

def parse_activity(line):
    return map(int, line.split())


def parse_testcase(input):
    num_ac, num_aj = map(int, input.readline().split())

    ac = []
    for _ in range(num_ac):
        ac.append(parse_activity(input.readline()))

    aj = []
    for _ in range(num_aj):
        aj.append(parse_activity(input.readline()))

    return (ac, aj)


def parse_testcases(input):
    num_testcases = int(input.readline())

    for _ in range(num_testcases):
        yield parse_testcase(input)


def solve_testcase(ac, aj):
    schedule = ([(start, end, "cameron") for start, end in ac] +
                [(start, end, "jamie") for start, end in aj])
    schedule.sort()

    gaps = [((s2 - e1) % (24 * 60), p1, p2) 
            for (_, e1, p1), (s2, _, p2) in zip(schedule, 
                                                schedule[1:] + [schedule[0]])]

    jamie_time = sum(end - start for start, end in ac)
    cameron_time = sum(end - start for start, end in aj)

    jamie_gaps = sorted([t for t, p1, p2 in gaps 
                         if p1 == "cameron" and p2 =="cameron"],
                        reverse=True)
    cameron_gaps = sorted([t for t, p1, p2 in gaps 
                           if p1 == "jamie" and p2 =="jamie"],
                           reverse=True)

    jamie_time += sum(jamie_gaps)
    cameron_time += sum(cameron_gaps)

    num_changes = sum(1 for _, p1, p2 in gaps if p1 != p2)

    while jamie_time > 12 * 60:
        jamie_time -= jamie_gaps.pop(0)
        num_changes += 2
    while cameron_time > 12 * 60:
        cameron_time -= cameron_gaps.pop(0)
        num_changes += 2

    return num_changes


def format_result(result):
    return "{:d}".format(result)


def main():
    testcases = parse_testcases(stdin)
    for num, testcase in enumerate(testcases, 1):
        result = solve_testcase(*testcase)
        print("Case #{}: {}".format(num, format_result(result)))        


if __name__ == "__main__":
    main()
