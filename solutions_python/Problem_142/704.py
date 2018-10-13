#!/usr/bin/env python

from pprint import pprint


def split(line):
    part = []
    for char in line:
        if part and part[-1] != char:
            yield len(part)
            part = []
        part.append(char)
    yield len(part)


def symbols(line):
    part = []
    for char in line:
        if part and part[-1] != char:
            yield part[0]
            part = []
        part.append(char)
    yield part[0]


def task(lines):
    chars = map(
        lambda line: list(symbols(line)),
        lines
    )
    lines = map(
        lambda line: list(split(line)),
        lines
    )

    l = len(lines[0])
    if not all(l == len(line) for line in lines):
        return 'Fegla Won'

    for chars in zip(*chars):
        if chars.count(chars[0]) != len(chars):
            return 'Fegla Won'

    count = 0
    for item in zip(*lines):
        count += max(item) - min(item)

    return count


def main():
    T = int(raw_input())
    for index in xrange(T):
        c = int(raw_input())
        lines = [
            raw_input()
            for _ in range(c)
        ]
        print 'Case #%d: %s' % (index + 1, task(lines))


if __name__ == '__main__':
    main()
