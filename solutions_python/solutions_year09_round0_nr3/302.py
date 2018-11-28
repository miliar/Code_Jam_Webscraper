#!/usr/bin/env python
#-*- coding: utf-8 -*-

def check(sentence, orig):
    if orig == '':
        return 1

    num = 0
    index = 0
    while True:
        index = sentence.find(orig[0], index)
        if index == -1:
            return num
        else:
            num += check(sentence[index+1:], orig[1:])
        index += 1

N = int(raw_input())

for i in range(N):
    orig = 'welcome to code jam'
    num = check(raw_input(), orig)
    print 'Case #%d: %s' % (i+1, str(num % 10000).zfill(4))
