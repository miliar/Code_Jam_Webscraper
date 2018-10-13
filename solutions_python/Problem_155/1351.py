#!/usr/bin/python
# coding: utf-8

import csv

def get_dataset(lines):
    data = []
    subset_st = 1
    for ss in zip(*[iter([l.strip() for l in lines])] * subset_st):
        l = ss[0].split()
        data.append({
            's_max': l[0],
            'audience': list([int(i) for i in l[1]]),
            })
    return data

def output(test_case, frends):
    print "Case #%s: %s" % (test_case, frends)

def main():
    with open('./input', 'r') as f:
        lines = f.readlines()
    test_num = lines[0]

    for i, d in enumerate(get_dataset(lines[1:]), 1):
        # print '----------------------'
        # print i,d['s_max'], d['audience']

        frends = 0
        stand  = 0
        for need, num in enumerate(d['audience']):
            if num == 0:
                continue
            if need > stand:
                frends +=  need - stand
                stand  += frends
            stand  += num
            #print '     (frends, stand): ', frends, stand
        output(i, frends)




if __name__ == '__main__':
    main()
