#! /usr/bin/python2.5
import sys

class LexNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
    def setWord(self, isWord):
        self.isWord = isWord
    def addChild(self, childLetter):
        if childLetter in self.children.keys():
            return
        newChild = LexNode()
        self.children[childLetter] = newChild
    def addWord(self, word):
        if len(word) == 0:
            self.isWord = True
        else:
            if word[0] not in self.children.keys():
                self.addChild(word[0])
            self.children[word[0]].addWord(word[1:])
    def isPrefix(self, word):
        if len(word) == 0:
            return True
        elif word[0] in self.children.keys():
            return self.children[word[0]].isPrefix(word[1:])
        else:
            return False
    def isAWord(self, word):
        if len(word) == 0:
            return self.isWord
        elif word[0] in self.children.keys():
            return self.children[word[0]].isAWord(word[1:])
        else:
            return False

class Lexicon:
    def __init__(self, wordlist):
        self.root = LexNode()
        self.numWords = 0
        for word in wordlist:
            self.addWord(word)
    def addWord(self, word):
        self.root.addWord(word)
        self.numWords += 1
    def isPrefix(self, word):
        return self.root.isPrefix(word)
    def isWord(self, word):
        return self.root.isAWord(word)

def numMatches(lex, pAsList, L):
    return recNumMatches('', lex, pAsList, L)

def recNumMatches(wordSoFar, lex, pAsList, L):
    if len(pAsList) == 0:
        if lex.isWord(wordSoFar):
            return 1
        return 0
    if not lex.isPrefix(wordSoFar):
        return 0

    if pAsList[0][0] != '(':
        return recNumMatches(wordSoFar+pAsList[0], lex, pAsList[1:], L)
    
    retNum = 0
    if pAsList[0][0] == '(':
        for ch in pAsList[0][1:-1]:
            retNum += recNumMatches(wordSoFar+ch, lex, pAsList[1:],L)
    return retNum

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print "Usage: CaseCounter.py infile"
    infname = sys.argv[1]
    f = open(infname)
    (L, D, N) = [int(n) for n in f.readline().split(' ')]
    words = []
    for i in range(D):
        words.append(f.readline().strip())
    lex = Lexicon(words)
    for j in range(1, 1+N):
        pattern = f.readline().strip().replace(')', ') ').replace('(', ' (')
        pAsList = [item for item in pattern.split(' ') if item != '']
        print "Case #%d: %d" % (j, numMatches(lex, pAsList, L))
