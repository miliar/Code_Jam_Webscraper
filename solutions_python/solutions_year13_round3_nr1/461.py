#! /usr/bin/env python3
# -*- coding: utf8 -*-
# vim: expandtab ts=4 ai

def do_detect(sstr,n):
    value = 0
    sstr = sstr.replace('a','_')
    sstr = sstr.replace('i','_')
    sstr = sstr.replace('u','_')
    sstr = sstr.replace('e','_')
    sstr = sstr.replace('o','_')
    sp_str = sstr.split('_')
    for e in sp_str:
        if len(e) >= n:
            value += 1
            break
    return value

def do_calc(name,n):
    val = 0
    for l in range(n,len(name)+1):
        for i in range(0,len(name)-l+1):
            sstr = name[i:(i+l)]
            val += do_detect(sstr,n)
    return val

def main():
    for c in range(int(input())):
        (name,n) = input().split()
        judge = do_calc(name,int(n))
        print('Case #%d: %s' % ( c+1, judge ))

if __name__ == '__main__':
    main()
