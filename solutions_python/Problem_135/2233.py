#!/usr/bin/env python
"""gcj code. """

from sys import stdin


def main():
    x = stdin.readline()
    y = int(x)
    for i in xrange(1, y + 1):
        print "Case #%d: %s" % (i, realmain(i))


def realmain(case):
    p1 = row()
    p2 = row()
    x = p1.intersection(p2)
    n = len(x)
    if n == 0:
        return "Volunteer cheated!"
    elif n > 1:
        return "Bad magician!"
    else:
        return x.pop()


def row():
    tr = int(stdin.readline())
    line = ''
    for i in xrange(1, 5):
        tmp = stdin.readline()
        if i == tr:
            line = tmp
    line = line.strip("\n")
    return set(line.split(' '))


#####################################################

if __name__ == '__main__':
    main()
