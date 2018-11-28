# Nikita Kouevda
# 2013/04/26

import sys


def main():
    if len(sys.argv) != 2:
        print('Please specify an input file')
        sys.exit(1)

    with open(sys.argv[1], 'r') as in_file:
        content = in_file.read().strip()

    lines = content.split('\n')
    cases = []

    for line in lines[1:]:
        line = line.strip().split()

        cases.append((int(line[0]), int(line[1])))

    for case_num, case in enumerate(cases):
        radius, volume = case

        a, b, c = 2, 2 * radius - 1, -volume

        solution = int((-b + int((b * b - 4 * a * c) ** 0.5)) / (2 * a))

        while True:
            if 2 * solution * solution + solution * b <= volume:
                break
            else:
                solution -= 1

        print('Case #{0}: {1}'.format(case_num + 1, solution))


if __name__ == '__main__':
    main()
