#!/usr/bin/env python


def standup(input):
    friends = 0
    count = 0

    for index, value in enumerate(input):
        value = int(value)

        while value > 0 and count < index:
            friends += 1
            count += 1
        count += value

    return friends

def main(lines):
    num_cases = int(lines[0])

    with open('large.out', 'w') as fh:
        for index, case in enumerate(lines[1:]):
            max_level, test = case.split()
            friends = standup(test)
            fh.write("Case #%s: %s\n" % (index + 1, friends))

if __name__ == '__main__':
    with open('large.in', 'r') as fh:
        lines = fh.readlines()

    main(lines)
