#!/usr/bin/python
import sys
import re
from collections import defaultdict

L, D, N = [int(n) for n in sys.stdin.readline().split()]

class Language:
    def __init__(self,D):
        """ D is the number of words in the language """
        self.d = {}
        self.table = [ defaultdict(set) for x in xrange(D)]

    def add_word(self,word):
        self.d[word] = True
        for i in xrange(len(word)):
            self.table[i][word[i]].add(word) # build index


    
    def match_c_at(self,index):
        """ self.table is a list of dictionaries, indexing the language
        by character position"""
        return self.table[index]

    def find_matches(self,index,pattern):
        """ return another set that contains the 
        subset of this language that matches the index at 'index'
        """
        possible = set()
        if pattern.isalpha():
            return self.table[index][pattern]
        else:
            for c in pattern[1:-1]: # strip off ( and )
###                print "possible before", possible
                possible.update(self.table[index][c])
###                print "possible after", possible
        return possible




def tokenise(pattern):
    """ Every word should have L tokens
    >>> tokenise("abc")
    ['a','b','c']
    >>> tokenise("a(bc)")
    ['a','bc']
    """
    RE = re.compile("\([a-z]+\)|[a-z]")
    return (tok.group() for tok in RE.finditer(pattern))
    
def find_matches(tok_stream, language):
    possible = set(language.d.keys() )
    for i,tok in enumerate(tok_stream):
         possible.intersection_update(language.find_matches(i,tok))
         if not len(possible):
             return 0
    return len(possible)






canon = Language(D)
for i in xrange(D):
    canon.add_word(sys.stdin.readline().strip())

for i in xrange(N):
    pattern  = sys.stdin.readline().strip()
    print "Case #%d: %d" % (i+1, find_matches(tokenise(pattern),canon))


