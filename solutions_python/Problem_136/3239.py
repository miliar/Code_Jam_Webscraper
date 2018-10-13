#!/usr/bin/python3


def next_line_to_flts(lines):
    return map(float, next(lines).split(' '))

f_in = open('b.in')
f_out = open('b.out', 'w')

lines = (i for i in f_in.read().splitlines())
t = int(next(lines))

for case in range(1, t+1):
    speed = 2
    time = 0
    c, f, x = next_line_to_flts(lines)
    while x/speed > c/speed + x/(speed + f):
        time += c/speed
        speed += f

    time += x/speed
    time = round(time, 7)

    f_out.write('Case #{!s}: {!s}\n'.format(case, time))
