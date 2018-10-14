#!/usr/bin/env python

import sys

file = open(sys.argv[1])

word_length, num_words, num_cases = map(int, file.readline().split())

def substrings(case):
    strings = []
    paren_flag = False
    substring = ''
    for char in case:
        if char == '(':
            paren_flag = True
            substring = ''
        elif char == ')':
            paren_flag = False
            strings.append(substring)
        elif paren_flag:
            substring += (char)
        else:
            strings.append(char)
    return strings

def num_matching_words(case):
    matches = 0
    case_strings = substrings(case)
    for word in words:
        match_flag = True
        for i in xrange(word_length):
            if word[i] not in case_strings[i]:
                match_flag = False
                break
        if match_flag:
            matches += 1
    return str(matches)
            
words = []
for i in xrange(num_words):
    words.append(file.readline().rstrip('\n'))

cases = []
for i in xrange(num_cases):
    cases.append(file.readline().rstrip('\n'))

case_number = 0
for case in cases:
    case_number += 1
    print 'Case #' + str(case_number) + ': ' + num_matching_words(case)
