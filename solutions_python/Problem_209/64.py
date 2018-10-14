from itertools import islice
from collections import namedtuple
from math import pi
from sys import stdin


Pancake = namedtuple("Pancake", ("radius", "height"))


def parse_pancake(line):
    return Pancake(*map(int, line.split()))


def parse_testcase(input):
    n, k = map(int, input.readline().split())

    pancakes = []
    for _ in range(n):
        pancakes.append(parse_pancake(input.readline()))

    return (k, pancakes)


def parse_testcases(input):
    num_testcases = int(input.readline())

    for _ in range(num_testcases):
        yield parse_testcase(input)


def solve_testcase(pancakes_needed, pancakes):
    pancakes.sort(key=lambda p: p.height*p.radius, reverse=True)

    main_pancakes = pancakes[:pancakes_needed-1]
    remainder = pancakes[pancakes_needed-1:]

    largest_r = max(p.radius for p in main_pancakes) if main_pancakes else 0

    def sort_key(p):
        result = 0
        if p.radius > largest_r:
            result += p.radius * p.radius - largest_r * largest_r
        result += 2 * p.radius * p.height
        return result

    best_remainder = max(remainder, key=sort_key)
    largest_r = max(largest_r, best_remainder.radius)

    pancakes = main_pancakes + [best_remainder]

    return  (pi * largest_r * largest_r + 
             sum(2 * pi * p.radius * p.height for p in pancakes))


def format_result(result):
    return "{:f}".format(result)


def main():
    testcases = parse_testcases(stdin)
    for num, testcase in enumerate(testcases, 1):
        result = solve_testcase(*testcase)
        print("Case #{}: {}".format(num, format_result(result)))        


if __name__ == "__main__":
    main()
