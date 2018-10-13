#!/usr/bin/python
# vi: set fileencoding=utf-8 :

'''
Google code jam 2015 qualification round
C: Dijkstra
'''

def prod(sign, symb, c):
    if symb == '1':
        if c == '1':
            return sign, '1'
        elif c == 'i':
            return sign, 'i'
        elif c == 'j':
            return sign, 'j'
        else:
            return sign, 'k'
    elif symb == 'i':
        if c == '1':
            return sign, 'i'
        elif c == 'i':
            return -1 * sign, '1'
        elif c == 'j':
            return sign, 'k'
        else:
            return -1 * sign, 'j'
    elif symb == 'j':
        if c == '1':
            return sign, 'j'
        elif c == 'i':
            return -1 * sign, 'k'
        elif c == 'j':
            return -1 * sign, '1'
        else:
            return sign, 'i'
    else:
        if c == '1':
            return sign, 'k'
        elif c == 'i':
            return sign, 'j'
        elif c == 'j':
            return -1 * sign, 'i'
        else:
            return -1 * sign, '1'


def broken_into_ijk(ijk, X):
    ijk *= X
    symb_i = ijk[0]
    sign_i = 1
    for i in range(1, len(ijk)):
        if sign_i == 1 and symb_i == 'i':
            symb_j = ijk[i]
            sign_j = 1
            for j in range(i + 1, len(ijk)):
                if sign_j == 1 and symb_j == 'j':
                    symb_k = ijk[j]
                    sign_k = 1
                    for c_k in ijk[j + 1:]:
                        sign_k, symb_k = prod(sign_k, symb_k, c_k)
                    if sign_k == 1 and symb_k == 'k':
                        return 'YES'
                    else:
                        break
                sign_j, symb_j = prod(sign_j, symb_j, ijk[j])
        sign_i, symb_i = prod(sign_i, symb_i, ijk[i])
    else:
        return 'NO'
        


T = int(raw_input())
for case_number in range(1, T + 1):
    L, X = map(int, raw_input().split())
    ijk = raw_input().rstrip()
    print 'Case #%d: %s' % (case_number, broken_into_ijk(ijk, X))
