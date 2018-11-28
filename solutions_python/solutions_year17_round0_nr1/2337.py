def print_case(idx, value):
    print("Case #{}: {}".format(idx, value))


def handle_problem(t, test_cases):
    for i in range(t):
        handle_test_case(i+1, test_cases[i])


def handle_test_case(idx, test_case):
    s, k = test_case.split()
    s = list(s)
    k = int(k)
    value = 0

    for i in range(len(s)):
        if check_pancakes(s):
            break

        if i + k > len(s):
            value = "IMPOSSIBLE"
            break

        if s[i] == '-':
            value += 1
            for j in range(i, i+k):
                s[j] = '-' if s[j] == '+' else '+'

    print_case(idx, value)


def check_pancakes(p):
    s = set(p)
    return len(s) == 1 and '+' in s


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
