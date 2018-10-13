import itertools
import sys

def solve(strings):
    set_strings = [''.join(c for c, _ in itertools.groupby(string)) for string
                  in strings]

    if len(set(set_strings)) != 1:
        return False

    value_strings = []
    for string in strings:
        value_strings.append([len(list(g)) for k, g in itertools.groupby(
            string)])

    count = 0
    for t in zip(*value_strings):
        count += abs(t[0] - t[-1])
    return count

def main():
    for tc in range(1, int(sys.stdin.readline()) + 1):
        N = int(sys.stdin.readline())
        strings = []
        for _ in range(N):
            strings.append(sys.stdin.readline().strip())

        result = solve(strings)
        if result is False:
            print("Case #{}: Fegla Won".format(tc))
        else:
            print("Case #{}: {}".format(tc, result))


if __name__ == '__main__':
    main()
