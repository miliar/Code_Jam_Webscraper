#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'duc_tin'
import re
import time

quater = {'jij':'i', 'iji':'j', 'jijiji':'k', 'iiii':'1',
          'kkkk':'1', 'jjjj':'1',
          '11': '1', '1i': 'i', '1j': 'j', '1k': 'k',
          'i1': 'i', 'ii': '-1', 'ij': 'k', 'ik': '-j',
          'j1': 'j', 'ji': '-k', 'jj': '-1', 'jk': 'i',
          'k1': 'k', 'ki': 'j', 'kj': '-i', 'kk': '-1',
          }


def intergrate(ijk):
    sign = 0

    while 1:
        if '-' in ijk:
            sign += ijk.count('-')
            ijk = ijk.replace('-', '')
        keys = [k for k in quater.keys() if len(k) <= len(ijk)]
        for key in sorted(keys, key=lambda k: len(k), reverse=1):
            # ijk = re.sub(key, quater[key], ijk)
            ijk = ijk.replace(key, quater[key])

        if len(ijk) == 1:
            break
        # else:
        #     ijk = quater[ijk[:2]]+ijk[2:]

    return '-'*(sign % 2)+ijk


def wait_char(char, start, min, str_in):
    index = start+1
    while 1:
        if index >= len(str_in)+1:
            return 'False'
        str_test = str_in[start:index]
        ret = intergrate(str_test)
        if ret == char and index >= min:
            # if str_test not in quater:
            #     quater[str_test] = char
            return index
        else:
            index += 1

T = int(raw_input())
t1 = time.time()
for case in range(T):
    L, X = [int(x) for x in raw_input().strip().split(' ')]
    sstr = raw_input().strip()
    string = sstr * X
    base = intergrate(sstr)
    res = 'NO'
    if len(set(sstr)) > 1 and base != '1' and len(string) > 2:
        mu = [m for m in (2,3,4,5) if X % m == 0]
        mu = 4 if 4 in mu else mu[0] if mu else 1
        if (base in 'ijk' and mu == 2) or (base in ['-i', '-j', '-k'] and mu == 2) or (base == '-1' and mu % 2 ==1):
            pointer_i = 1
            # print sstr, X
            while pointer_i < len(string):
                    first_half = string[:pointer_i]
                    second_half = string[pointer_i:]
                    if intergrate(first_half) == 'i':
                        pointer_j = 1
                        while pointer_j < len(second_half):
                            second_half_f = second_half[:pointer_j]
                            second_half_s = second_half[pointer_j:]
                            if intergrate(second_half_f) == 'j' and intergrate(second_half_s) == 'k':
                                res = 'YES'
                                break
                            else:
                                pointer_j += 1

                        if res == 'YES':
                            break
                    pointer_i += 1

    print 'Case #%s: %s' % (case+1, res)  #, base, X, intergrate(string)
# print time.time() - t1