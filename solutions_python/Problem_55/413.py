'''
Created on May 8, 2010

@author: francesccampoyflores
'''

import sys

class Queue:
    def __init__(self, list):
        self.l = list
        self.n = len(list)
        self.i = 0
    
    def start(self):
        self.first = self.i
        
    def next(self):
        self.i = (self.i+1)%self.n
        return self.i != self.first
    
    def current(self):
        return self.l[self.i]
        
if __name__ == '__main__':
    input = open(sys.argv[1],'r')
    output = open(sys.argv[2], 'w')
    
    T = int(input.readline())
    for t in range(1, T+1):
        R, k, _ = map(int, input.readline().split())
        q = Queue(map(int, input.readline().split()))
        res = 0
        
        for r in range(R):
            m = 0
            q.start()
            while True:
                m += q.current()
                if not q.next():
                    break
                if m + q.current() > k:
                    break
            res += m

        output.write("Case #%d: %d\n"%(t, res))