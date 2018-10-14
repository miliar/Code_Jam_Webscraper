#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import sys

def debug(a): sys.stderr.write(str(a) + '\n')
def readarray(foo): return [foo(e) for e in raw_input().split()]
def readint(): return int(raw_input().strip())



def calc(table, size):
    score = []
    for team in xrange(size):
        win = 0
        lose = 0
        for opponent in xrange(size):
            if table[team][opponent] == '1':
                win += 1
            elif table[team][opponent] == '0':
                lose += 1
        score.append((win, lose))
        debug('{0}: {1}'.format(team, score[team]))

    wp = [float(win) / (win + lose) for win, lose in score]
    debug(wp)

    owp = []
    for team in xrange(size):
        tmp = []
        for opponent in xrange(size):
            if table[team][opponent] == '.':
                continue
            op_win = score[opponent][0]
            op_lose = score[opponent][1]
            if table[opponent][team] == '1':
                op_win -= 1
            else:
                op_lose -= 1
            tmp.append(float(op_win) / (op_win + op_lose))
        owp.append(sum(tmp) / len(tmp))
        debug('{0}: {1}'.format(team, owp[team]))

    oowp = []
    for team in xrange(size):
        tmp = []
        for opponent in xrange(size):
            if table[team][opponent] == '.':
                continue
            tmp.append(owp[opponent])
        oowp.append(sum(tmp) / len(tmp))
        debug('{0}: {1}'.format(team, oowp[team]))


    return (0.25 * wp[team] + 0.5 * owp[team] + 0.25 * oowp[team] \
                for team in xrange(size))


T = readint()
for i in xrange(T):
    N = readint()
    table = []
    for j in xrange(N):
        table.append(raw_input())
    debug(table)

    print('Case #{0}:'.format(i + 1,))
    for v in calc(table, N):
        print(v)
