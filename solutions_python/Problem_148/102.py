#!/usr/bin/python3


def next_line_to_ints(lines, delimiter=' '):
    return map(int, next(lines).split(delimiter))

f_in = open('a.in')
f_out = open('a.out', 'w')

lines = (i for i in f_in.read().splitlines())
t = int(next(lines))


for case in range(1, t+1):
    n, x = next_line_to_ints(lines)
    files = next_line_to_ints(lines)
    files = sorted(files, reverse=True)

    discs = []

    while files:
        first = files.pop()
        last = 0
        if first <= x/2:
            for i, f in enumerate(files):
                if f + first <= x:
                    last = i
                    last = files.pop(last)
                    break

        discs.append((first, last))

    answer = len(discs)

    f_out.write('Case #{!s}: {!s}\n'.format(case, answer))
