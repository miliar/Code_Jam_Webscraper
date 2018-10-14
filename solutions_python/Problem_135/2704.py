#-*- coding: utf-8 -*-


import sys

_in = sys.stdin

def get_line(line):
    lines = []
    i = 4
    while i:
        lines.append([int(x) for x in _in.readline().split(" ")])
        i -= 1
    return lines[line-1]

def solve():
    ans1 = get_line(int(_in.readline()))
    ans2 = get_line(int(_in.readline()))

    result = [x for x in ans1 if x in ans2]

    if len(result) == 0:
        return "Volunteer cheated!"
    elif len(result) == 1:
        return str(result[0])
    else:
        return "Bad magician!"

T = int(_in.readline());
Ti = 1

while Ti <= T:
    print "Case #%d: %s" % (Ti, solve())
    Ti += 1


