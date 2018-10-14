import math

__author__ = 'Benjamin S.'


fi = open('input.txt', 'r')
fo = open('output.txt', 'w')


def read_line():
    return fi.readline()


def write_line(line):
    fo.write(line + "\n")


def output():
    numbers = map(int, read_line().split(" "))
    a = numbers[0]
    b = numbers[1]
    k = numbers[2]

    pairs = 0
    for i in range(a):
        for j in range(b):
            if i & j < k:
                pairs += 1

    return pairs


C = int(read_line())
for c in range(C):
    write_line("Case #%s: %s" % (c+1, output()))