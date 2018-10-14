#!/usr/local/bin/python
import argparse
from itertools import islice
from heapq import *
from collections import deque
from itertools import ifilter
import copy

def main():
    # Take input
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()

    # Read input
    cases = []
    with open(args.input) as f:
        n = int(f.readline())
        for i in range(n):
            cases.append("".join(list(islice(f, 3))))

    # Handle cases
    handleCases(cases)

def handleCases(cases):
    for i, case in enumerate(cases):
        print "Case #{n}: {result}".format(n=i+1, result=handleCase(case))

def handleCase(case):
    # Set up blocks
    inp = filter(None, case.split("\n"))
    n = int(inp[0])
    naomi = deque(heapsort([float(x) for x in inp[1].split(" ")]))
    ken = deque(heapsort([float(x) for x in inp[2].split(" ")]))

    # Optimal War
    a = copy.copy(naomi)
    b = copy.copy(ken)
    owarpoints = 0
    for i in range(n):
        # Naomi chooses smallest block
        nblock = a.popleft()
        # Ken chooses next biggest
        kblock = next(ifilter(lambda x: x > nblock, b), None)
        if kblock is None:
            owarpoints += 1
        else:
            b.remove(kblock)
    # Deceptive War
    a = copy.copy(naomi)
    b = copy.copy(ken)
    dwarpoints = 0
    decr = .000001
    for i in range(n):
        # Naomi chooses smallest block, says it's .000001 less than largest Ken
        if a[-1] > b[-1]:
            a.pop()
            b.pop()
            dwarpoints += 1
        else:
            realnblock = a.popleft()
            kblock = b.pop()
            fakenblock = (kblock - decr) if kblock > realnblock else realnblock
            if fakenblock > kblock:
                dwarpoints += 1
    return '{} {}'.format(dwarpoints, owarpoints)

def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

if __name__ == "__main__":
    main()
