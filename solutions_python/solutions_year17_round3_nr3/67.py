from itertools import islice
from collections import namedtuple
from sys import stdin

def parse_activity(line):
    return map(int, line.split())


def parse_testcase(input):
    n, k = map(int, input.readline().split())
    u = float(input.readline())

    ps = map(float, input.readline().split())

    return (k, u, ps)


def parse_testcases(input):
    num_testcases = int(input.readline())

    for _ in range(num_testcases):
        yield parse_testcase(input)


def solve_testcase(cores_to_function, training_units, probabilities):
    probabilities.sort()

    num_cores = len(probabilities)

    for index in range(num_cores):
        next_prob = probabilities[index+1] if index+1 < num_cores else 1.0
        increment = min(training_units / (index + 1), 
                        next_prob - probabilities[index])

        for subindex in range(index+1):
            probabilities[subindex] += increment
            training_units -= increment

    prob = 1
    for p in probabilities:
        prob *= p

    return prob


def format_result(result):
    return "{:f}".format(result)


def main():
    testcases = parse_testcases(stdin)
    for num, testcase in enumerate(testcases, 1):
        result = solve_testcase(*testcase)
        print("Case #{}: {}".format(num, format_result(result)))        


if __name__ == "__main__":
    main()
