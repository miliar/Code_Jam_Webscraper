#!/usr/bin/env python

from __future__ import with_statement

def match(pattern, word):
    if '(' not in pattern:
        return pattern == word
    j = 0
    for i in range(0, len(word)):
        if pattern[j] != '(':
            if pattern[j] != word[i]:
                return False
            else:
                j += 1
        else:
            j += 1
            pos = []
            for k in range(j, len(pattern)):
                if pattern[k] == ')':
                    j = k + 1
                    break
                else:
                    pos.append(pattern[k])
            if word[i] not in pos:
                return False
    return True

def main():
    with open('A-large.in..txt', 'r') as stream:
        inp = stream.read().split('\n')

    numbers = inp[0].split(' ')
    words = inp[1:int(numbers[1]) + 1]
    patterns = inp[len(words) + 1:]

    for i in range(0, len(patterns) - 1):
        matching = 0
        for word in words:
            if match(patterns[i], word):
                matching += 1
        print 'Case #%d: %d' % (i+1, matching)

if __name__ == '__main__':
    main()
