import sys
import time
import re

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

def runCase(inpFile):
    caseLine = inpFile.readline().split(" ")
    combinations = {}
    if caseLine[0] != "0":
        combinationString = caseLine[1]
        for i in range(0, len(combinationString), 3):
            left, right, result = combinationString[i], combinationString[i+1], combinationString[i+2]
            combinations[left+right] = result
            combinations[right+left] = result
        caseLine = caseLine[1:]
    eliminations = {}
    if caseLine[1] != "0":
        eliminationString = caseLine[2]
        for i in range(0, len(eliminationString), 2):
            left, right = eliminationString[i], eliminationString[i+1]
            eliminations[left] = right
            eliminations[right] = left
        caseLine = caseLine[1:]
    result = []
    invocations = caseLine[3]
    for c in invocations:
        result.append(c)
        if len(result) > 1:
            tail = "".join(result[-2:]) 
            if tail in combinations:
                result = result[:-2] + [combinations[tail]]
                continue
        if c in eliminations:
            if eliminations[c] in result:
                result = []
    print "[" + ", ".join(result) + "]"
            
#@timerWrap
def main():
    inpFile = InputReader(open("magicka.in", "r"))
    sys.stdout = Tee(sys.stdout, open("magicka.out", "w"))
    for index in inpFile.readcases():
        print "Case #%d:" % index, 
        runCase(inpFile)
        sys.stdout.flush()

main()
