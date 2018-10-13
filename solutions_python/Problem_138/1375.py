#!/usr/bin/env python

import sys

def getl():
    return sys.stdin.readline().strip()

def gt(l, x):
    '''filter items from l that are greater than x'''
    return [i for i in l if i > x]

def play(strategy, naomi, ken):

    if len(naomi) != len(ken):
        exit('players have different number of bricks!')

    war = (strategy.lower()[0] == 'w')

    l_naomi = list(sorted(naomi))
    l_ken =   list(sorted(ken))
    naomi_score = 0

    for i in range(len(l_naomi)):

        # naomi move
        if war:
            naomi_move = naomi_move_told = l_naomi.pop(0)
        else:
            if max(l_naomi) > max(l_ken):
                naomi_move = l_naomi.pop(l_naomi.index(min(gt(l_naomi, l_ken[-1]))))
                naomi_move_told = l_ken[-1] - 0.00005
            # if min(l_naomi) < min(l_ken):
            else:
                naomi_move = l_naomi.pop(0)
                naomi_move_told = l_ken[-1] - 0.000005

        # ken move
        ken_heavier = [x for x in l_ken if x > naomi_move_told]

        if ken_heavier:
            ken_move = l_ken.pop(l_ken.index(min(ken_heavier)))
        else:
            ken_move = l_ken.pop(l_ken.index(min(l_ken)))

        if naomi_move > ken_move:
            naomi_score += 1

        # if naomi_move == naomi_move_told:
        #     print("MOVE: %s : %s" % (naomi_move, ken_move))
        # else:
        #     print("MOVE: %s (%s) : %s" % (naomi_move, naomi_move_told, ken_move))

        if naomi_move_told > ken_move > naomi_move:
            exit('ken: %s, naomi: %s but told: %s!' % (ken_move, naomi_move, naomi_move_told))

    if len(l_ken) > 0:
        exit('ken has %i remaining bricks after the game!' % (len(l_ken),))
    if len(l_naomi) > 0:
        exit('naomi has %i remaining bricks after the game!' % (len(l_naomi),))

    return naomi_score


n = int(getl())

for i in range(n):
    x = i + 1

    n = int(getl())
    l1 = list(map(float, getl().split(' ')))
    l2 = list(map(float, getl().split(' ')))
    if len(l1) != n:
            exit('Naomi got %i bricks instead of %i' % (len(l1), n))
    if len(l2) != n:
            exit('Ken got %i bricks instead of %i' % (len(l2), n))

    r = (play('deceitful', l1, l2),
         play('war',       l1, l2),
        )

    if r[0] < r[1]:
        exit('Naomi deceit did not work (%s vs %s)' % (r[0], r[1]))

    print('Case #%i: %s %s' % (x, r[0], r[1]))


