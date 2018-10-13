#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Problem1():
    def run(self, wires):
        print wires
        a_ends = map(lambda (a, b): a, wires)
        b_ends = map(lambda (a, b): b, wires)
        
        if len(wires) == 1:
            return 0

        if len(wires) == 2:
            if a_ends[0] < a_ends[1] and b_ends[0] < b_ends[1]:
                return 0
            if a_ends[0] > a_ends[1] and b_ends[0] > b_ends[1]:
                return 0
            return 1

        return 3

if __name__ == "__main__":
    solver = Problem1()
    results = []

    with open("A-small-attempt0.in") as in_file:
        t = int(in_file.readline())
        for i in range(t):
            n = int(in_file.readline())
            wires = []
            for j in range(n):
                a, b = map(int, in_file.readline().split(' '))
                wires.append((a, b))
            result = solver.run(wires)
            results.append(result)

    with open("ouput.txt", "w") as out_file:
        for i in range(len(results)):
            line = "Case #%s: %s\n" % (i + 1, results[i])
            out_file.write(line)