#!/usr/bin/python
# coding: utf-8

import csv

def get_dataset(lines):
    data = []
    subset_st = 1
    for ss in zip(*[iter([l.strip() for l in lines])] * subset_st):
        l = ss[0].split()
        data.append({
            'X': int(l[0]),
            'R': int(l[1]),
            'C': int(l[2])
            })
    return data

def output(test_case, win):
    if win == 'g':
        print "Case #%s: GABRIEL" % (test_case)
    elif win == 'r':
        print "Case #%s: RICHARD" % (test_case)

def main():
    with open('./input', 'r') as f:
        lines = f.readlines()
    test_num = lines[0]

    for i, d in enumerate(get_dataset(lines[1:]), 1):
        gflag = False
        if d['R'] * d['C'] >= d['X']         and\
           d['R'] * d['C'] % d['X'] == 0    and\
           d['X'] < 8                       and\
           d['X'] < min([d['R'], d['C']]) +2:
            gflag =True

        if gflag:
            output(i, 'g')
        else:
            output(i, 'r')




if __name__ == '__main__':
    main()
