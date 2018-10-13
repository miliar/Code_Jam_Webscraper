#!/usr/bin/env python
from pdb import set_trace
from collections import deque
import sys

def run(R, k, G):

    euros = 0

    D = deque(G)
    passengers = deque()

    def lap():

        while True:
            if not D: # D is empty
                break
            p = D.popleft()
            passengers.append(p)
            if sum(passengers) > k:
                # on enleve le dernier convoi
                D.appendleft(p)
                passengers.pop()
                break

    if False:
        lap()
        print 'lap1', passengers, D, sum(passengers)
        D.extend(passengers)
        passengers.clear()

        lap()
        print 'lap2', passengers, D, sum(passengers)
        D.extend(passengers)
        passengers.clear()

    while R > 0:
        lap()
        euros += sum(passengers)

        D.extend(passengers)
        passengers.clear()

        R -= 1

    return euros

if __name__ == '__main__':
    assert run(4, 6, [1, 4, 2, 1]) == 21

    lines = open('in.txt').read().splitlines()
    S = int( lines[0] )
    j = 1
    c = 1
    for i in range(S):

        line = map(int, lines[j].split())
        R = line[0]
        k = line[1]
        G = map(int, lines[j+1].split())

        sys.stderr.write('%d\n' % c)
        print 'Case #%d: %s' % (c, run(R, k, G))

        j += 2
        c += 1
