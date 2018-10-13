#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from copy import copy

def lost_func(word):
    global alph, word_list
    cur_re = ['.'] * len(word)
    cur_wl = [w for w in word_list if len(w) == len(word)]
    r = ''.join(cur_re)
    assert all(re.match(r, w) for w in cur_wl)

    points = 0
    guessed = ''
    needguess = len(set(word))
    for a_i,a in enumerate(alph):
        if not any(a in w for w in cur_wl):
            continue
        if a in word:
            guessed += a
            for i, c in enumerate(word):
                if c == a:
                    cur_re[i] = a
                else:
                    cur_re[i] = "[^%s]" % a
            r = ''.join(cur_re)
            cur_wl = [w for w in cur_wl if re.match(r, w)]
            if len(guessed) == needguess:
                return points
        else:
            cur_wl = [w for w in cur_wl if a not in w]
            points += 1
    raise RuntimeError

testcount = int(sys.stdin.readline())
for i in xrange(testcount):
    case = i + 1
    N, M = map(int, sys.stdin.readline().strip().split())
    word_list = []
    for _ in xrange(N):
        word = sys.stdin.readline()
        word_list.append(word.strip())

    res_lst = []
    for _ in xrange(M):
        alph = sys.stdin.readline().strip()
        curres = max(word_list, key=lost_func)
        res_lst.append(curres)
    print "Case #%d: %s" % (case, ' '.join(res_lst))
