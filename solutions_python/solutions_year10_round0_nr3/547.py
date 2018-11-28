#!/usr/bin/python

import math
import sys

from collections import deque

def main():

    f = open(sys.argv[1])
    numTests = int(f.readline())

    lines = f.readlines()
    for i in range(numTests):

        (r, k, n) = lines[2 * i].split()
        tests = lines[2 * i + 1].split()

        queue = deque()
        for item in tests:
            queue.append(int(item))

        r = int(r)
        n = int(n)
        k = int(k)

        total = 0

        for j in range(r):
            soFar = 0
            thisTime = 0
            while thisTime < n:
                next = queue.popleft()
                if soFar + next > k:
                    queue.appendleft(next)
                    break
                else:
                    soFar += next
                    queue.append(next)
                thisTime += 1
            total += soFar

        print "Case #" + str(i + 1) + ": " + str(total)
    
if __name__ == "__main__":
    main()
