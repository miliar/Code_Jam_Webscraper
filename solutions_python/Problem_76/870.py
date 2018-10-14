""" Uri Shaked """

import sys
import time
import re
from itertools import permutations

try:
    import psyco
    psyco.full()
except ImportError:
    pass

class Tee(object): 
    def __init__(self, *fds):
        self._fds = fds
    
    def write(self, data):
        for fd in self._fds:
            fd.write(data)

    def flush(self):
        for fd in self._fds:
            fd.flush()
    
    def close(self):
        for fd in self._fds:
            fd.close()

class InputReader(object):
    def __init__(self, f):
        self.f = f
    
    def readline(self):
        return self.f.readline().strip()
    
    def readnlines(self):
        entryCount = int(self.readline())
        for i in range(0, entryCount):
            yield self.readline()
        
    def readints(self):
        return list(map(int, self.readline().split(" ")))
    
    def readmatrix(self, rows, linetrans=lambda x:x):
        return [linetrans(self.readline()) for i in range(rows)]
    
    def readcases(self):
        entryCount = int(self.readline())
        for i in range(1, entryCount + 1):
            yield i

def timerWrap(func):
    def __inner(*args,**kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            print >> sys.stderr, "Runtime: %.3f sec" % (time.time() - start)
    return __inner

def xorList(list):
    result = 0
    for element in list:
        result ^= element
    return result

def runCase(inpFile):
    inpFile.readline()
    candies = inpFile.readints()
    if xorList(candies) == 0:
        print sum(candies)-min(candies)
    else:
        print "NO"

#@timerWrap
def main():
    inpFile = InputReader(open("candy.in", "r"))
    sys.stdout = Tee(sys.stdout, open("candy.out", "w"))
    for index in inpFile.readcases():
        print "Case #%d:" % index, 
        runCase(inpFile)
        sys.stdout.flush()

main()
