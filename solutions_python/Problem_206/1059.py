#!/usr/bin/python3
from __future__ import print_function
import sys

debug = True
debug = False



lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

n = int(lines[0])
currentLine = 1
for i in range(n):
    destination, horses = list(map(int, lines[currentLine].split(' ')))
    currentLine += 1
    
    if debug: print('#' * 20)
    if debug: print(destination, horses)

    horsesSpeeds = []
    maxDuration = 0
    for h in range(horses):
        start, speed = list(map(int, lines[currentLine].split(' ')))
        duration = (destination - start) / speed
        horsesSpeeds.append([start, speed, duration])
        if duration > maxDuration:
            maxDuration = duration
        currentLine += 1
    if debug: print(horsesSpeeds)
    
    print('Case #' + str(i+1) + ': ' + str(round(destination / maxDuration, 6)))
