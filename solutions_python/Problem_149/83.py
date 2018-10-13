#!/usr/bin/python3

# This was helpfull: http://stackoverflow.com/questions/20990127/


def next_line_to_ints(lines, delimiter=' '):
    return map(int, next(lines).split(delimiter))


def count_inversions(items):
    inversions = 0
    for i, n in enumerate(items):
        for m in items[i + 1:]:
            if n > m:
                inversions += 1
    return inversions


f_in = open('b.in')
f_out = open('b.out', 'w')

lines = (i for i in f_in.read().splitlines())
t = int(next(lines))

for case in range(1, t+1):
    next(lines)
    numbers = list(next_line_to_ints(lines))
    answer = 0

    middle = max(numbers)
    middle_index = numbers.index(middle)

    first = numbers[:middle_index]
    last = numbers[middle_index + 1:]

    for i, n in enumerate(numbers):
        if i is middle_index:
            continue

        begin = 0
        end = 0

        for m in numbers[:i]:
            if m > n:
                begin += 1

        for m in numbers[i + 1:]:
            if m > n:
                end += 1

        answer += min((begin, end))

    f_out.write('Case #{!s}: {!s}\n'.format(case, answer))
