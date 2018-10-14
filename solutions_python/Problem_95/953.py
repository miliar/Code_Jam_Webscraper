#!/usr/bin/env python
# encoding: utf-8

import sys


alpha  = "abcdefghijklmnopqrstuvwxyz"
google = "ynficwlbkuomxsevzpdrjgthaq"

G = int(sys.stdin.readline())

middleWord = []
finalWord = []

for i in range(G):
    words = map(str,sys.stdin.readline().split())
    print 'Case #%d: ' % (i+1), 
    for word in words:
        for letter in word:
            sys.stdout.write(alpha[google.index(letter)])
        sys.stdout.write(" ")
    sys.stdout.write("\n")
                # 
                #         middleWord = "".join(finalWord) + "".join(alpha[index])
                #     finalWord.append(middleWord)
                # 
                # print 'Case #%d: %s ' % (i+1, ' '.join(map(str,finalWord)))
                #     
            
            