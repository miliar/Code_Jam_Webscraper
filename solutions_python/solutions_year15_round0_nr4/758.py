#!/usr/bin/python
# -*- coding: utf-8 -*-
# †
import enum

class Player(str, enum.Enum):
    R = 'RICHARD'
    G = 'GABRIEL'

T = int(raw_input())
players = [Player.R, Player.G]
for case in xrange(T):
    X, R, C = map(int, raw_input().split())
    R, C = min(R, C), max(R, C)
    if X == 1:
        res = players[1]
    elif X == 2:
        # 0で割り切れる→埋めることができる→後手の勝ち
        res = players[(R * C) % 2 == 0]
    elif X == 3:
        if min(R, C) == 1:
            res = players[0]
        else:
            res = players[(R * C) % 3 == 0]
    else:
        if min(R, C) == 1:
            res = players[0]
        elif min(R, C) == 4:
            res = players[1]
        elif R == 3 and C == 4:
            res = players[1]
        else:
            res = players[0]
    print 'Case #{}: {}'.format(case+1, res)
