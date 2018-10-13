#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin

def is_palindrome(word):
    reverseword = ''

    for i in xrange(len(word)):
        reverseword += word[-i-1]

    return reverseword == word

if __name__ == "__main__":
    ncases = int(stdin.readline())

    for ncase in xrange(ncases):
        n, m = map(int, stdin.readline().split(' '))

        lawn = [[] for j in xrange(n)]

        for row in xrange(n):
            lawn[row] = map(int, stdin.readline().split(' '))

        allle = True

        for row in xrange(n):
            for column in xrange(m):

                hle = True
                vle = True
                for frow in xrange(n):
                    if lawn[frow][column] > lawn[row][column]:
                        vle = False
                for fcolumn in xrange(m):
                    if lawn[row][fcolumn] > lawn[row][column]:
                        hle = False

                allle = hle or vle

                if not allle:
                    break
            if not allle:
                break

        result = 'YES' if allle else 'NO'
        print 'Case #' + str(ncase + 1) + ': ' + result

                
