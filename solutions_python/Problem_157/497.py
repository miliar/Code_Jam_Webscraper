import sys
import os

mul_dict = {'11':'1', '1i':'i',  '1j':'j',  '1k':'k',
            'i1':'i', 'ii':'-1', 'ij':'k',  'ik':'-j',
            'j1':'j', 'ji':'-k', 'jj':'-1', 'jk':'i',
            'k1':'k', 'ki':'j',  'kj':'-i', 'kk':'-1'}

def mul(l, r):
    signed = False
    if l[0] is '-':
        signed = not signed
        l = l[1]
    if r[0] is '-':
        signed = not signed
        r = r[1]
    res = mul_dict[l+r]
    if res[0] is '-':
        signed = not signed
        res = res[1]
    return ('-' if signed else '') + res

def print_result(c, b):
    print('Case #%d: %s' % (c, ('Yes' if b else 'No')))

def __main__():
    case_number = int(input())
    for case in range(case_number):
        line = input()
        L = int(line.split(' ')[0])
        X = int(line.split(' ')[1])
        repeat = ((X%4 + 8) if X > 12 else X)
        line = input()
        eval_str = line * repeat
        if len(eval_str) < 3:
            print_result(case+1, False)
            continue
        
        reduce = '1'
        i_reduced = False
        k_reduced = False
        for i in range(len(eval_str)):
            reduce = mul(reduce, eval_str[i])
            if not i_reduced and reduce is 'i':
                i_reduced = True
            if i_reduced and not k_reduced and reduce is 'k':
                k_reduced = True
        print_result(case+1, ((reduce == '-1') and i_reduced and k_reduced))

sys.stdin = open('C-large.in', 'r')
sys.stdout = open('C-large.out', 'w')
__main__()
