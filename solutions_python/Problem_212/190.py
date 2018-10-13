from sys import stdin

def parse_testcase(input):
    N, P = map(int, input.readline().strip().split())
    groups = map(int, input.readline().strip().split())

    return P, groups

def parse_testcases(input):
    num_testcases = int(input.readline())

    for _ in range(num_testcases):
        yield parse_testcase(input)

def solve_testcase(num_pieces, groups):
    offsets = [0 for _ in range(num_pieces)]

    for group in groups:
        offsets[group % num_pieces] += 1

    result = 0

    queue = [[x] for x in range(num_pieces)]
    while queue:
        components = queue.pop(0)

        divisors = [sum(1 for x in components if x == y) 
                    for y in components]
        counts = [offsets[c] / d for c, d in zip(components, divisors)]
        min_count = min(counts)

        if min_count == 0:
            continue

        if sum(components) % num_pieces == 0:
            result += min_count
            for c in components:
                offsets[c] -= min_count
        else:
            for index in range(components[-1], num_pieces):
                queue.append(components + [index])

    if any(count > 0 for count in offsets):
        result += 1

    return result


def format_result(result):
    return "{:d}".format(result)


def main():
    testcases = parse_testcases(stdin)
    for num, testcase in enumerate(testcases, 1):
        result = solve_testcase(*testcase)
        print("Case #{}: {}".format(num, format_result(result)))        


if __name__ == "__main__":
    main()
