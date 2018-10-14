#!/usr/bin/env python
# encoding: utf-8
"""
" Problem B in quialification round of google codejam 2015
" Author: Tsirif
"""

import math

def finished(d, p):
    if d == 0:
        return True
    else:
        return False


def normal(d, p):
    d = 0
    a = []
    for i in p:
        tmp = i - 1
        if tmp != 0:
            a.append(tmp)
            d += 1
    return d, a


def special(d, p, iMax, part):
    s = p[iMax] / part
    p[iMax] = p[iMax] - s
    p.append(s)
    d += 1
    return d, p


def check_worst_y(d, p):
    return max(p)


def next_node(d, p, y):
    y += 1
    # print
    # print "Y = "+str(y)
    # print "D : "+str(d)
    # print "P : "+str(p)
    # if finished(d, p):
    #     return y
    max_p = max(p)
    best_y = max_p  # normal
    best_choice = [1]
    if (max_p <= 3):
        # print "return normal: "+str(1 + best_y)
        # print best_choice
        return (1 + best_y, best_choice)
    i = p.index(max_p)
    part = 1
    # limit = int(math.sqrt(max_p))
    limit = max_p / 2
    while part + 1 <= limit:
        part += 1
        # print "Y = "+str(y)+" part = "+str(part)
        special_D, special_P = special(int(d), list(p), i, part)
        y_special, special_choice = next_node(special_D, special_P, y)
        if y_special < best_y:
            best_y = y_special
            best_choice = special_choice
            best_choice.insert(0, part)
        else:
            break
    # print "return y: "+str(y)+" part: "+str(part)+" "+str(1 + best_y)
    # print best_choice
    return (1 + best_y, best_choice)


T = int(raw_input())
for i in xrange(1, T+1):
    D = int(raw_input())
    P = map(int, raw_input().split())
    assert len(P) == D

    # worst_case_Y = 0
    # while not finished(D, P):
    #     # print
    #     # print "D : "+str(D)
    #     # print "P : "+str(P)
    #     worst_case_Y = check_worst_y(D, P) - 1  # normal case
    #     special_D, special_P = best_special(int(D), list(P))
    #     # print "special_D: "+str(special_D)
    #     # print "special_P: "+str(special_P)
    #     if check_worst_y(special_D, special_P) < worst_case_Y:
    #         D = special_D
    #         P = special_P
    #     else:
    #         D, P = normal(D, P)
    #     Y += 1
    Y, best_choices = next_node(D, P, -1)

    print "Case #"+str(i)+": "+str(Y-1)
    # print best_choices
