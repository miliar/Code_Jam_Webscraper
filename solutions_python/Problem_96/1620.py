#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: Álvaro Lázaro


def main():
    out = ""

    with open('in.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        for i in xrange(1, n + 1):
            numbers = lines[i].split()
            googlers = numbers[0]
            surprising = numbers[1]
            p = numbers[2]
            out += "Case #%s: %s\n" % (i, max_googlers(numbers[3:],
                int(surprising), int(p)))

    with open('out.txt', 'w') as out_file:
        out_file.write(out)

def max_points(total, objective):
    max_points = None
    points = total / 3
    if total == 0:
        return {False: 0, True: 0}
    elif total == 1:
        return {False: 1, True: 1}
    if total == 2:
        return {False: 1, True: 2}
    rest = total % 3
    if rest == 0:
        max_points = {False: points, True: points + 1}
    elif rest == 1:
        max_points = {False: points + 1, True: points + 1}
    elif rest == 2:
        max_points = {False: points + 1, True: points + 2}
    return max_points


def max_googlers(googlers, s, p):
    count = 0
    surp_count = 0
    for g in googlers:
        g_points = max_points(int(g), p)
        if g_points[False] >= p:
            count += 1
        elif surp_count < s and g_points[True] >= p:
            count += 1
            surp_count += 1
    return count


if __name__ == '__main__':
    main()
