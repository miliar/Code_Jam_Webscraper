import fileinput


def solve(case):
    max_shy, ppl = case.split()
    current_value = 0
    current_invited = 0
    for i, count in enumerate(map(int, ppl)):
        if count and current_value < i:
            current_invited += (i - current_value)
            current_value = i
        current_value += count
    return current_invited


def main():
    for i, case in enumerate(fileinput.input()):
        if i > 0:
            print("Case #{}: {}".format(i, solve(case)))

if __name__ == '__main__':
    main()
