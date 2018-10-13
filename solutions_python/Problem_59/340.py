'''
Created on May 22, 2010

@author: jagadeesh
'''

import sys
from sys import stdin

class Problem:
    
    def __init__(self):
        self.T = 0
        self.N = 0
        self.M = 0
        
        self.case = 0
        self.root = {}
        self.count = 0
    
    
    def _readT(self):
        self.T = int(stdin.readline())
    
    
    def _readNM(self):
        line = stdin.readline()
        self.N, self.M = [int(x) for x in line.split()]
    
    
    def __call__(self):
        
        self._readT()
        self.case = 0
        
        for x in range(self.T):
            self._readNM()
            self.case += 1
            yield self.case

    
    def solve(self):
        self.root = {}
        self.count = 0
        
        for x in range(self.N):
            self.mkdir()
        
        self.count = 0
        
        for x in range(self.M):
            self.mkdir()
        
        print "Case #%s: %s" % (self.case, self.count)
    
    
    
    def mkdir(self):
        path = stdin.readline()
        
        path = path.strip()
        if path == '/': # corner case
            return
        
        dirs = path.split('/')

        root = self.root
        for dir in dirs:
            if dir == '':
                continue
            
            if not root.has_key(dir):
                root[dir] = {}
                self.count += 1

            root = root[dir]
        


if __name__ == "__main__":
    
    problem = Problem()
    for case in problem():
        problem.solve()
    
