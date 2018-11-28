#!/usr/bin/env python
# encoding: utf-8
"""
a_alien_language.py

Created by Robert Wallis on 2009-09-02.
Copyright (c) 2009 Robert Wallis. All rights reserved.
"""
L, D, N = list(int(i) for i in raw_input().split())

words = []
for i in range(0, D):
    words.append(raw_input())

for case in range(1, N+1):
    pattern = raw_input()
    answer = 0
    
    # analyze the pattern
    tokens = []
    token = ""
    inside_parenthesis = False
    for i in range(0, len(pattern)):
        if pattern[i] == '(':
            inside_parenthesis = True
        elif pattern[i] == ')':
            inside_parenthesis = False
            if len(token): tokens.append(token)
            token = ""
        else:
            if inside_parenthesis:
                token += pattern[i]
            else:
                tokens.append(pattern[i])

    usable = {}
    for i in range(0, len(words)):
        usable[words[i]] = True
    for w in words:
        for l in range(0, L):
            if w[l] not in tokens[l]:
                usable[w] = False
                break
    for w in words:
        if usable[w]:
            answer += 1
    print('Case #%d: %s' % (case, answer))