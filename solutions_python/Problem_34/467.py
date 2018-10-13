#import math
import sys
#import random


def GetNumMatches(pattern, words):
    patternPos = 0
    for wordPos in range(0,L):
        # find all good characters for the wordPos position
        goodChar = set()
        if pattern[patternPos]=='(':
            while pattern[patternPos]!= ')':
                patternPos += 1
                goodChar.add(pattern[patternPos])
        else:
            goodChar.add(pattern[patternPos])
        patternPos += 1
        
        #remove from words the non-matches
        allWords = words.copy()
        for w in allWords:
            if w[wordPos] not in goodChar:
                words.remove(w)
    return str(len(words))

def processFile(source, target):
    global L # Length of each word

    sf = open(source)
    tf = open(target,"w")
    [L,D,N] = sf.readline().strip('\n').split(' ')
    L = int(L)
    D = int(D)
    N = int(N)
    realWords = set()
    for i in range(0,D):
        w = sf.readline()
        realWords.add(w)
    for case in range(1,N+1):
        p = sf.readline() # read pattern 
        patternsRealWords = realWords.copy()
        result = GetNumMatches(p, patternsRealWords)
        newline = 'Case #' + repr(case) + ': ' + result
        #print(newline)
        tf.write(newline)
        if not case==N: tf.write('\n')
    sf.close
    tf.close


def main(argv = None):
    if argv is None:
        argv = sys.argv
    if (len(argv)>2):
        processFile(argv[1], argv[2])
    
if __name__ == "__main__":
    main()
    