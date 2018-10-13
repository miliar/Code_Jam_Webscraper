__author__ = 'dkopiychenko'

import os


def number_of_friends(l):
    c = 0
    r = 0
    for i in range(len(l)):
        if i > c:
            r += 1
            c += 1
        c += l[i]
    return r



with open(os.path.expanduser("~/gcj2015/input01l.txt")) as f:
    n = f.readline().strip('\n')
    print n
    lines = [x.strip('\n') for x in f.readlines()]
    counter = 1
    for l in lines:
        a, b = l.split(' ')
        g = [int(x) for x in b]
        print 'Case #' + str(counter) + ': ' + str(number_of_friends(g))
        counter += 1