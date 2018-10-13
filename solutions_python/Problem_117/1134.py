#! /usr/local/bin/python2.7
import sys
import os

if len(sys.argv) < 2: sys.exit(-1)
if not os.path.isfile(sys.argv[1]): sys.exit(-2)

f = open(sys.argv[1])

num_inputs = int(f.readline())

for case in range(num_inputs):
    dim = map(int, f.readline().split())
    lawn = []
    for _ in range(dim[0]):
        lawn.append(map(int, f.readline().split()))

    max_x = {}
    for x in range(dim[1]):
        maximum = 0
        for y in range(dim[0]):
            if lawn[y][x] > maximum:
                maximum = lawn[y][x]
        max_x[x] = maximum
    max_y = {}
    for y in range(dim[0]):
        maximum = 0
        for x in range(dim[1]):
            if lawn[y][x] > maximum:
                maximum = lawn[y][x]
        max_y[y] = maximum

    # The position needs to be >= all in either row or col
    possible = True
    for y in range(dim[0]):
        if not possible: break
        for x in range(dim[1]):
            if lawn[y][x] < max_x[x] and lawn[y][x] < max_y[y]:
                possible = False
                break
    print "Case #%i: %s" % (case + 1, 'YES' if possible else 'NO')
