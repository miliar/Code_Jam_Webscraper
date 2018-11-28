""" Uri Shaked """

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

def normalize(word, letters):
    return re.sub("[^%s]" % letters, "_", word)

def runCase(inpFile):
    N, M = inpFile.readints()
    words = [inpFile.readline() for i in range(N)]
    letterSets = [inpFile.readline() for i in range(M)]
    wordSets = {}
    for word in words:
        if len(word) not in wordSets:
            wordSets[len(word)] = []
        wordSets[len(word)].append(word)
    #print wordSets
    for letters in letterSets:
        scores = []
        for candidate in words:
            wordSet = list(wordSets[len(candidate)])
            
            if len(wordSet) == 1:
                scores.append([candidate, 0])
                continue
            score = 0
            guessed = ""
            for letter in letters: 
                if letter in "".join(wordSet):
                    if letter not in candidate:
                        score += 1
                    guessed += letter
                    normalizedCandidate = normalize(candidate, guessed)
                    wordSet = [word for word in wordSet if normalize(word, guessed) == normalizedCandidate]
                    if len(wordSet) == 0:
                        break
            scores.append([candidate, score])
        print max(scores, key = lambda x:x[1])[0],
            
    print ""

#@timerWrap
def main():
    inpFile = InputReader(open("hangman.in", "r"))
    sys.stdout = Tee(sys.stdout, open("hangman.out", "w"))
    for index in inpFile.readcases():
        print "Case #%d:" % index, 
        runCase(inpFile)
        sys.stdout.flush()

try:
    import psyco
    psyco.full()
except ImportError:
    pass
main()
