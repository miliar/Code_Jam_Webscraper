#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from math import log, ceil

class Problem2():
    def run(self, l, p, c):
        step_counter = 0
        left = l

        while left < p:
            left *= c
            step_counter += 1

        return int(ceil(log(step_counter, 2)))

if __name__ == "__main__":
    solver = Problem2()
    results = []

    with open("B-large.in") as in_file:
        t = int(in_file.readline())
        for i in range(t):
            l, p, c = map(int, in_file.readline().split(' '))
            result = solver.run(l, p, c)
            results.append(result)

    with open("ouput.txt", "w") as out_file:
        for i in range(len(results)):
            line = "Case #%s: %s\n" % (i + 1, results[i])
            out_file.write(line)