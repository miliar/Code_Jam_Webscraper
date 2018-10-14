#! /usr/bin/env python


def main():
    with open('a.in', 'r') as fin, open('a.out', 'w') as fout:
        num_cases = int(fin.readline())
        for case in range(1, num_cases + 1):
            shy_string = fin.readline().split()[1]
            answer = solve(shy_string)
            fout.write('Case #{0}: {1}\n'.format(case, answer))


def solve(shy_string):
    num_guests = num_standing = 0
    for shy_level, num_audience in enumerate(shy_string):
        if num_standing >= shy_level:
            num_standing += int(num_audience)
        elif num_audience != '0':
            num_guests += shy_level - num_standing
            num_standing += (int(num_audience) + shy_level - num_standing)
    return num_guests


if __name__ == '__main__':
    main()
