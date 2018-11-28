#!/usr/bin/python
# coding: utf-8

import csv

def get_dataset(lines):
    data = []
    subset_st = 2
    for ss in zip(*[iter([l.strip() for l in lines])] * subset_st):
        l = ss[0].split()
        data.append({
            'L': l[0],
            'X': l[1],
            'string': list(ss[1] * int(l[1]))
            })
    return data

def output(test_case, res):
    if res == 0:
        print "Case #%s: YES" % (test_case)
    else:
        print "Case #%s: NO" % (test_case)


def get_conv_start(string):
    if string[0] != 'i':
        return 0
    elif string[1] != 'j':
        return 1
    elif string[2] != 'k':
        return 2
    else:
        return 3

def exe_conv(substring, sign):
    conv_dict = {'i': {'i':[],    'j':['k'], 'k':['j']},
                 'j': {'i':['k'], 'j':[],    'k':['i']},
                 'k': {'i':['j'], 'j':['i'], 'k':[]},
                 }
    sign_dict = {'i': {'i':-1, 'j': 1, 'k':-1},
                 'j': {'i':-1, 'j':-1, 'k': 1},
                 'k': {'i': 1, 'j':-1, 'k':-1},
                 }
    fs = substring[0]
    ss = substring[1]

    return  sign_dict[fs][ss] * sign, conv_dict[fs][ss] + substring[2:]


def evaluate(string, sign):
    if (len(string) < 3) or ((len(string) == 4) and string[:3] == list('ijk')):
        return 2  # stop error
    elif string == list('ijk'):
        if sign < 0:
            return 2  # stop error
        else:
            return 0  # stop success
    else:
        return 1  # continue

def main():
    with open('./input', 'r') as f:
        lines = f.readlines()
    test_num = lines[0]

    for i, d in enumerate(get_dataset(lines[1:]), 1):
        target_string = d['string']
        sign   = 1
        result = evaluate(target_string, sign)

        #print '----------------------'
        while result == 1:
            tnum = get_conv_start(target_string)
            #print tnum, ''.join(target_string), ' => ',
            prf = target_string[:tnum]
            sign, tmp_string = exe_conv(target_string[tnum:], sign)
            target_string = prf + tmp_string

            result = evaluate(target_string, sign)
            #print result, len(target_string)
            #print sign, ''.join(target_string), result
        output(i, result)

if __name__ == '__main__':
    main()
