# -*- coding: utf-8 -*-

"""
File : qual1.py
Author : Sergei Lebedev <superbobry@gmail.com>
Created : Чтв, Сен  3 2009 by Sergei Lebedev
Description : Alien Language

"""

from re import compile, findall

brackets = compile(r'\((\w+)\)')

if __name__ == '__main__':
    data = open('A-large.in').read().split('\n')
    L, D, N = map(int, data[0].split(' '))
    words = data[1:D+1]
    wordsline = ' '.join(words)

    for case in xrange(1, N+1):
        pattern, count = data[D + case], 0

        if not brackets.search(pattern):
            if pattern in words:
                count = 1
        else:
            count = len(findall(
                brackets.sub(r'[\1]', pattern), wordsline))

        print 'Case #%i: %i' % (case, count)




