#! /usr/bin/env python

#usage: cat input | this_program > output

import sys

num_testcases = int(sys.stdin.readline())

### main
for case in range(1, num_testcases + 1):
    data = sys.stdin.readline().split()
    N = int(data[0])
    data = zip(data[1::2], map(int, data[2::2]))
    def move_time(robot):
        posses = [1] + [p for r, p in data if r == robot]
        m_t = map(lambda start, stop: abs(stop - start),
                      posses[:-1], posses[1:])
        return m_t
    m_t = {"O": move_time("O"), "B": move_time("B")} #move time
    a_t = {"O": 0, "B": 0} #time after last push is done
    for r, p in data:
        if r == "O":
            other = "B"
        else:
            other ="O"
        ready_to_push = a_t[r] + m_t[r].pop(0)
        ready_to_push = max(ready_to_push, a_t[other])
        a_t[r] = ready_to_push + 1
    result = max(a_t["O"], a_t["B"])
    print "Case #%i: %i" %(case, result)
