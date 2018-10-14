def print_case(idx, value):
    print("Case #{}: {}".format(idx, value))


def handle_problem(t, test_cases):
    for i in range(t):
        handle_test_case(i+1, test_cases[i])


def handle_test_case(idx, test_case):
    nl = [int(ni) for ni in test_case]

    for i in range(len(nl)-1, 0, -1):
        if i - 1 < 0:
            break

        if nl[i] < nl[i-1]:
            nl[i-1] -= 1
            for j in range(i, len(nl)):
                nl[j] = 9

    print_case(idx, int(''.join([str(v) for v in nl])))


if __name__ == "__main__":
    import sys

    file_path = sys.argv[1]

    T = 0
    test_cases = list()

    with open(file_path) as f:
        lines = f.read().splitlines()
        T = int(lines[0])
        test_cases = lines[1:]

    # Redirect to file
    sys.stdout = open("{}_out".format(file_path), 'w')

    handle_problem(T, test_cases)
