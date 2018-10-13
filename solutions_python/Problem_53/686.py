#!/usr/bin/env python

import sys

def is_powered(snappers, position):
    return all(snappers[:position])

def step(snappers):
    new_snappers = snappers[:]
    for i in xrange(len(new_snappers)-1, 0-1, -1):
        if all(snappers[:i]):
            new_snappers[i] = snappers[i] ^ 1
    return new_snappers

def snapper_run(size, snaps):
    snappers = [0] * size
    for i in xrange(snaps):
        snappers = step(snappers)
    return sum(snappers) == size
	
def main():
    i = 0
    results = []
    T = int(sys.stdin.readline())
    for line in sys.stdin:
        N, K = line.split()
        results.append(snapper_run(int(N), int(K)))
        i = i + 1
        if i >= T:
            break
    for i, result in enumerate(results):
        print "Case #%d: " % (i + 1, ),
        if result:
            print "ON"
        else:
            print "OFF"

if __name__ == '__main__':
	main()
