#!/usr/bin/python

import sys
from collections import deque

baseFilename = sys.argv[1]

fIn = file(baseFilename + '.in')
fOut = file(baseFilename + '.out', 'w')

num_tests = int(fIn.readline().strip())

current_test = 1;
while current_test <= num_tests:
    (Runs, Capacity, Groups) = fIn.readline().strip().split(' ')
    Runs = int(Runs); Capacity = int(Capacity); Groups = int(Groups)
    
    temp = fIn.readline().strip().split(' ')
    queue = deque()
    riders = deque()
    for value in temp:
        queue.append(int(value))
    current_run = 0
    total_riders = 0
    while current_run < Runs:
        current_riders = 0
        while True:
            if len(queue) > 0 and current_riders + queue[0] <= Capacity:
                riders.append(queue.popleft())
                current_riders += riders[-1]
            else:
                break
        total_riders += current_riders
        queue.extend(riders)
        riders.clear()
        current_run += 1

    fOut.write("Case #%d: %d\n" % (current_test, total_riders) );
    current_test += 1;

fOut.close();
fIn.close();