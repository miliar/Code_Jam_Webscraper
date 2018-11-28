#! /usr/bin/env python

import sys
from bisect import bisect_left

class Trie:
    def __init__(self, alpha) :
        self.alpha = alpha
        self.next = []

    def list(self) :
        d = [ self.alpha ]
        for i in self.next : d.append(i.list())
        return d

    def __str__(self) :
        return repr(self.list())

    def find_alpha(self, alpha) :
        return bisect_left([i.alpha for i in self.next], alpha)

    def add_word(self, word) :
        p = self.find_alpha(word[0])
        if ( p == len(self.next) or self.next[p].alpha != word[0] ) :
            self.next.insert(p, Trie(word[0]))
        if ( word[1:] ) :
            self.next[p].add_word(word[1:])

    def find_word(self, word) :
        if ( word[0] == '(' ) :
            count = 0;
            end = word.index(')', 1)
            for i in word[1:end] :
                p = self.find_alpha(i)
                if ( p == len(self.next) or self.next[p].alpha != i ) :
                    pass
                else :
                    if ( word[end + 1:] ) :
                        count += self.next[p].find_word(word[end + 1:])
                    else :
                        count += 1
            return count
        else :
            p = self.find_alpha(word[0])
            if ( p == len(self.next) or self.next[p].alpha != word[0] ) :
                return 0
            if ( word[1:] ) :
                return self.next[p].find_word(word[1:])
            else :
                return 1


if ( len(sys.argv) > 1 ) :
    file = open(sys.argv[1], "r")
else :
    file = sys.stdin

L, D, N = [int(i) for i in file.readline().rstrip().split()]

trie = Trie("")
for i in range(D) :
    trie.add_word(file.readline().rstrip())

for i in range(1, N + 1) :
    print "Case #" + str(i) + ":", trie.find_word(file.readline().rstrip())

file.close()


