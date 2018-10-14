#!/usr/bin/python
# -*- encoding: utf-8 -*-

import sys

Length, Dictionary, Number_of_cases = map(int, sys.stdin.readline().split())

map = []
for i in xrange(Length):
    tmp = []
    for j in xrange(26):
        tmp.append(set())
    map.append(tmp)

# map[index][char]
orda = ord('a')

for wordno in xrange(Dictionary):
    word = sys.stdin.readline().strip()
    for index, char_ in enumerate(word):
        char = ord(char_) - orda
        map[index][char].add(wordno)

for testno in xrange(Number_of_cases):
    test = sys.stdin.readline().strip()

    index = 0
    matches = []
    while test:
        if test[0] == '(':
            i = test.index(')')
            check_chars = test[1:i]
            test = test[i+1:]
        else:
            check_chars = test[0]
            test = test[1:]
        matching_letters = set()
        for char_ in check_chars:
            char = ord(char_) - orda
            matching_letters.update(map[index][char])
        matches.append(matching_letters)
        index += 1

    intersect = matches.pop()
    while matches:
        intersect = intersect.intersection(matches.pop())
    print "Case #%i: %i" % (testno+1, len(intersect))

# vim:set tabstop=4 softtabstop=4 shiftwidth=4 expandtab: 
