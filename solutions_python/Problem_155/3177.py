#!/usr/bin/env python3

__author__ = 'Yatharth Agarwal <yatharth999@gmail.com>'

def f(ms, ss):
    counter = 0
    stood = 0
    for level, people in enumerate(map(int, ss)):
        if level > stood:
            counter += level - stood
            stood = level
        stood += people
    return counter



filename = 'large'
with open('{}.in'.format(filename)) as infile, open("{}.out".format(filename), 'w') as outfile:
    read = lambda: infile.readline().strip()

    t = int(read())
    for i in range(1, t+1):
        ms, ss = read().split()
        o = f(ms, ss)
        outfile.write("Case #{}: {}\n".format(i, o))
