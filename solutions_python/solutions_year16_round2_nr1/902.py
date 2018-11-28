
import csv
import itertools
import copy
import time
import numpy as np


def read_file(filename):
    f = open(filename)
    csv_r = csv.reader(f, delimiter=' ')
    T = int(csv_r.next()[0])
    test_lst = []
    for i in xrange(T):
        L = csv_r.next()
        test_lst.append(''.join(L).upper())
    f.close() 
    return test_lst 


def solve_test(test_case):
    d={}
    for e in test_case:
        if e not in d:
            d[e]=0
        d[e]+=1
    l=[0]*10
    if d.get('Z',0)>0:
        l[0]=d['Z']
        for e in 'ZERO':
            d[e]-=l[0]
    if d.get('X',0)>0:
        l[6]=d['X']
        for e in 'SIX':
            d[e]-=l[6]
    if d.get('G',0)>0:
        l[8]=d['G']
        for e in 'EIGHT':
            d[e]-=l[8]
    if d.get('W',0)>0:
        l[2]=d['W']
        for e in 'TWO':
            d[e]-=l[2]
    if d.get('H',0)>0:
        l[3]=d['H']
        for e in 'THREE':
            d[e]-=l[3]
    if d.get('U',0)>0:
        l[4]=d['U']
        for e in 'FOUR':
            d[e]-=l[4]
    if d.get('O',0)>0:
        l[1]=d['O']
        for e in 'ONE':
            d[e]-=l[1]
    if d.get('S',0)>0:
        l[7]=d['S']
        for e in 'SEVEN':
            d[e]-=l[7]
    if d.get('V',0)>0:
        l[5]=d['V']
        for e in 'FIVE':
            d[e]-=l[5]
    if d.get('N',0)>0:
        l[9]=d['N']/2
        for e in 'NINE':
            d[e]-=l[9]
    for e,v in d.items():
        if v != 0:
            print e, v
            raise
    r=[]
    for i_v, v in enumerate(l):
        if v==0:
            continue
        r.extend([str(i_v)]*v)
    
    return "".join(r)
        

def main(filename):
    test_lst = read_file(filename)
    for i_test, test_case in enumerate(test_lst):
        res = solve_test(test_case)
        print "Case #%i: %s" % (1+i_test, res)


if __name__ == '__main__':
    #main('./simple.in')
    #main('./A-small-attempt2.in')
    main('./A-large.in')


