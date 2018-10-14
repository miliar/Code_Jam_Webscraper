#!/usr/bin/env python
import sys

class Lawn:
    n = 0
    m = 0
    field = []
    def __init__(self, n, m, data):
        self.n = n
        self.m = m
        self.field = [[0 for j in range(self.m)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                self.field[i][j] = data[i][j]

    def state(self):
        for i in range(self.n):
            for j in range(self.m):
                height = self.field[i][j]
                xok = True
                yok = True
                for x in range(self.n):
                    if self.field[x][j] > height:
                        xok = False
                for y in range(self.m):
                    if self.field[i][y] > height:
                        yok = False
                if xok == False and yok == False:
                    return "NO"
                
        return "YES"

size = int(input())
tests = []
for i in range(size):
    line = sys.stdin.readline().strip()
    n = int(line.split()[0])
    m = int(line.split()[1])

    data = [];
    for j in range(n):
        data.append(sys.stdin.readline().strip().split())
    tests.append(Lawn(n, m, data))

i = 1
for test in tests:
    print "Case #" + str(i) + ": " + test.state()
    i = i + 1
