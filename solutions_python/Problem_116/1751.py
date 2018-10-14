#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin

def merge(a,b):
    if a == b:
        return a
    elif a == 'T':
        return b
    elif a == '.':
        return '.'
    else:
        return '-'

def first_row(h,v,d):
    row = stdin.readline()

    h[0] = row[0]
    v[0] = row[0]

    for i in xrange(1,4):
        h[0] = merge(row[i], h[0])
        v[i] = row[i]

    d[0] = row[0]
    d[1] = row[3]

def process_row(rown,h,v,d):
    row = stdin.readline()

    h[rown] = row[0]
    v[0] = merge(row[0], v[0])

    for i in xrange(1,4):
        h[rown] = merge(row[i], h[rown])
        v[i] = merge(row[i], v[i])

    d[0] = merge(row[rown], d[0])
    d[1] = merge(row[3-rown], d[1])

def who_won(who,h,v,d = ''):
    if h == who or v == who or d == who:
        return True
    return False


if __name__ == "__main__":
    ncases = int(stdin.readline())

    for ncase in xrange(ncases):

        h = ['','','','']
        v = ['','','','']
        d = ['','']

        winner = '.'

        first_row(h,v,d)

        for rown in xrange(1,4):
            process_row(rown,h,v,d)

        row = stdin.readline()

        winner = '-'

        for i in xrange(2):
            if who_won('X',h[i],v[i],d[i]):
                winner = 'X'
                break
            elif who_won('O',h[i],v[i],d[i]):
                winner = 'O'
                break
            elif who_won('.',h[i],v[i],d[i]):
                winner = '.'

        if winner == '.':
            for i in xrange(2,4):
                if who_won('X',h[i],v[i]):
                    winner = 'X'
                    break
                elif who_won('O',h[i],v[i]):
                    winner = 'O'
                    break
                elif who_won('.',h[i],v[i]):
                    winner = '.'

        if winner == '.':
            print 'Case #' + str(ncase + 1) + ': Game has not completed'
        elif winner == '-':
            print 'Case #' + str(ncase + 1) + ': Draw'
        else:
            print 'Case #' + str(ncase + 1) + ': ' + winner + ' won'


