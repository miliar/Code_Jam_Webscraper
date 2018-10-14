#!/usr/bin/python3


def next_line_to_ints(lines):
    return map(int, next(lines).split(' '))

f_in = open('a.in')
f_out = open('a.out', 'w')

lines = (i for i in f_in.read().splitlines())
t = int(next(lines))

for case in range(1, t+1):
    a = int(next(lines))
    for i in range(1, 5):
        if i == a:
            answers = set(next_line_to_ints(lines))
        else:
            next(lines)

    a = int(next(lines))

    for i in range(1, 5):
        if i == a:
            answers = answers.intersection(next_line_to_ints(lines))
        else:
            next(lines)

    if len(answers) == 1:
        a = list(answers)[0]
    elif len(answers) == 0:
        a = 'Volunteer cheated!'
    else:
        a = 'Bad magician!'

    f_out.write('Case #{!s}: {!s}\n'.format(case, a))
