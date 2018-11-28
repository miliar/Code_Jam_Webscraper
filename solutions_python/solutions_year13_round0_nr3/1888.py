#!/usr/bin/env python
import sys
import math

class FairAndSquare:
    f = 0
    t = 0
    def __init__(self, f, t):
        self.f = f
        self.t = t
        
    def isFair(self, i):
        data = str(i)
        size = len(data)
        for i in range(int(math.floor(size / 2))):
            if str(data[i]) != str(data[size - i - 1]):
                return False
        return True

    def state(self):
        count = 0
        i = int(math.ceil(math.sqrt(self.f)))
        while(i*i <= self.t):
            if self.isFair(i):
                if self.isFair(i*i):
                    count = count + 1
            i = i + 1
        return str(count)

size = int(input())
tests = []
for i in range(size):
    line = sys.stdin.readline().strip()
    f = int(line.split()[0])
    t = int(line.split()[1])

    data = [];
    tests.append(FairAndSquare(f, t))

i = 1
for test in tests:
    print "Case #" + str(i) + ": " + test.state()
    i = i + 1
