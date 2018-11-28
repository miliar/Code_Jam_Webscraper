import math
import operator

from sys import stdin

def printAnswer(caseIndex, answer):
    print("Case #", caseIndex+1, ": ", answer, sep='')

def mult(sign_a, a, sign_b, b):
    values = {
        '1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
        'i': {'1': 'i', 'i': '1', 'j': 'k', 'k': 'j'},
        'j': {'1': 'j', 'i': 'k', 'j': '1', 'k': 'i'},
        'k': {'1': 'k', 'i': 'j', 'j': 'i', 'k': '1'},
    }
    signs = {
        '1': {'1': 0, 'i': 0, 'j': 0, 'k': 0},
        'i': {'1': 0, 'i': 1, 'j': 0, 'k': 1},
        'j': {'1': 0, 'i': 1, 'j': 1, 'k': 0},
        'k': {'1': 0, 'i': 0, 'j': 1, 'k': 1},
    }
    return (sign_a + sign_b + signs[a][b]) % 2, values[a][b]

T = int(input())
for t in range(T):
    L, X = map(int, input().split())
    s = input()
    s *= X

    i_found, j_found, k_found = False, False, False
    
    r = '1'
    sign_r = 0
    k_stop = 0
    for i, l in enumerate(reversed(s)):
        sign_r, r = mult(0, l, sign_r, r)
        if sign_r == 0 and r == 'k':
            k_found = True
            k_stop = i
            break

    k_stop += 1
        
    r = '1'
    sign_r = 0
    for l in s[:-k_stop]:
        sign_r, r = mult(sign_r, r, 0, l)
        if not i_found and sign_r == 0 and r == 'i':
            i_found = True
            r = '1'
            sign_r = 0

    if sign_r == 0 and r == 'j':
        j_found = True

    if i_found and j_found and k_found:
        printAnswer(t, 'YES')
    else:
        printAnswer(t, 'NO')
