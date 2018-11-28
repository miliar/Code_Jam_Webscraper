#!/usr/bin/env python


def build(list):
    dict={}
    sl = sorted(list)
    for i in range(len(sl)):
        dict[sl[i]] = i
    return dict

def comp(list):
    miss = 0
    dict = build(list)
    for i in range(len(list)):
        if dict[list[i]] != i:
            miss += 1
    return miss

if __name__ == '__main__':
    f = open('input')
    a = int( f.readline() )
    for cn in range(a):
        f.readline()
        list = map(int,f.readline().split())
        print "Case #"+str(cn+1)+":", comp(list)

