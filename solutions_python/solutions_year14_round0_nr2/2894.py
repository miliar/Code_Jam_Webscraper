#!/usr/bin/env python
# -*- coding: utf-8 -*-

input = open("input.txt", "r")
output = open("output.txt", "w")

t = int(input.readline().strip())
for i in range(t):
    c, f, x = map(float, input.readline().strip().split())
    speed = 2.0
    time = 0.0
    while x > 0.0:
        time += c / speed
        x -= c
        if (x + c) / (f + speed) >= x / speed:
            time += x / speed
            break
        x += c
        speed += f
    str = 'Case #%d: %f' % (i + 1, time)
    output.write(str + "\n")

input.close()
output.close()
