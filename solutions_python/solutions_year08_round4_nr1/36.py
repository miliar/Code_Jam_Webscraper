import psyco
psyco.full()

class Leaf:
    def __init__(self, value):
        self.value = value
        
    def getValue(self):
        return self.value
    
    def getMinCostToZero(self):
        if self.value == 0:
            return 0        
        return 1000000000
    
    def getMinCostToOne(self):
        if self.value == 1:
            return 0        
        return 1000000000

class Node:
    def __init__(self, s):
        self.g, self.c = map(int, s.split(" "))
        self.left = None
        self.right = None
        self.min_to_zero = None
        self.min_to_one = None
        
    def getMinCost(self):
        if self.getValue() == 0:
            return self.getMinCostToOne()
        return self.getMinCostToZero()
    
    def getMinCostToZero(self):
        if self.min_to_zero is not None:
            return self.min_to_zero
        value = self.getValue()
        if value == 0:
            self.min_to_zero = 0
            return self.min_to_zero        
        if self.g == 1:
            self.min_to_zero = min(self.left.getMinCostToZero(), self.right.getMinCostToZero())
            return self.min_to_zero
        if self.c == 1 and self.g == 0:
            self.min_to_zero = min(self.left.getMinCostToZero(), self.right.getMinCostToZero()) + 1
            return self.min_to_zero            
        self.min_to_zero = self.left.getMinCostToZero() + self.right.getMinCostToZero()
        return self.min_to_zero
    
    def getMinCostToOne(self):
        if self.min_to_one is not None:
            return self.min_to_one
        value = self.getValue()
        if value == 1:
            self.min_to_one = 0
            return self.min_to_one
        if self.g == 0:
            self.min_to_one = min(self.left.getMinCostToOne(), self.right.getMinCostToOne())
            return self.min_to_one
        if self.c == 1 and self.g == 1:
            self.min_to_one = min(self.left.getMinCostToOne(), self.right.getMinCostToOne()) + 1
            return self.min_to_one
        self.min_to_one = self.left.getMinCostToOne() + self.right.getMinCostToOne()
        return self.min_to_one
    
    def getValue(self):
        if self.g == 1:
            return self.left.getValue() and self.right.getValue()
        else:
            return self.left.getValue() or self.right.getValue()

class Case:
    def __init__(self, s):
        self.m, self.v = map(int, s.read().split(" "))
        self.interiors = s.readList((self.m - 1) / 2)
        self.leaves = map(int, s.readList((self.m + 1) / 2))

    def solve(self):
        nodes = [Node(i) for i in self.interiors]
        for ix in range(1, len(nodes)):
            i = ix + 1
            if i % 2 == 1:
                nodes[int(i / 2) - 1].right = nodes[ix]
            else:
                nodes[int(i / 2) - 1].left = nodes[ix]
        for ix in range(len(self.leaves)):
            i = len(nodes) + ix + 1
            if i % 2 == 1:
                nodes[int(i / 2) - 1].right = Leaf(self.leaves[ix])
            else:
                nodes[int(i / 2) - 1].left = Leaf(self.leaves[ix])
        if self.v == 0:
            cost = nodes[0].getMinCostToZero()
        else:
            cost = nodes[0].getMinCostToOne()
        if cost > 50000000:
            return "IMPOSSIBLE"
        return "%d" % cost

class Contents:
    def __init__(self, f):
        self.data = [line.strip() for line in f]
        self.i = 0

    def read(self):
        return self.readList(1)[0]

    def readList(self, len):
        result = self.data[self.i : self.i + len]
        self.i += len
        return result

import sys
f = file(sys.argv[1])
s = Contents(f)
numCases = int(s.read())

for caseNum in range(numCases):
    case = Case(s)
    print "Case #%d: %s" % (caseNum + 1, case.solve())
