#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 KuoE0 <kuoe0.tw@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import itertools

def LCS(str1, str2):

    dp_table = [[0 for j in xrange(len(str2) + 1)] for i in xrange(len(str1) + 1)]
    for i in xrange(len(str1)):
        for j in xrange(len(str2)):
            dp_table[i + 1][j + 1] = dp_table[i][j] + 1 if str1[i] == str2[j] else max(dp_table[i + 1][j], dp_table[i][j + 1])

    return max([max(v) for v in dp_table])

def removeSameAdj(string):

    dup_flag = [1 for i in xrange(len(string))]
    for i in xrange(len(string) - 1):
        if string[i] == string[i + 1]:
            dup_flag[i] = 0

    return ''.join(itertools.compress(string, dup_flag))

def isSameCharOrder(string_list):
    for str1 in string_list:
        for str2 in string_list:
            if removeSameAdj(str1) != removeSameAdj(str2):
                return False
    return True

T = input()

for t in xrange(T):

    N = input()

    string_list = [raw_input() for i in xrange(N)]
    
    if not isSameCharOrder(string_list):
        print 'Case #{0}: Fegla Won'.format(t + 1)
        continue

    lcs_table = [[LCS(string_list[i], string_list[j]) if i != j else -1 for j in xrange(N)] for i in xrange(N)]

    min_lcs = min([x for x in itertools.chain(*lcs_table) if x >= 0])
    max_lcs = max([x for x in itertools.chain(*lcs_table) if x >= 0])

    ret = min([sum([abs(len(s) - l) for s in string_list]) for l in range(min_lcs, max_lcs + 1)])

    print 'Case #{0}: {1}'.format(t + 1, ret)





