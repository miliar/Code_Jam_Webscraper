#! /usr/bin/env python
# -*- coding: utf8 -*-
# vim: expandtab ts=4 ai

GAIN_RATE = 2.0

def do_calc(c,f,x):

    rate = GAIN_RATE
    estimate = x / rate
    pre_firm = 0.0

    while( True ):
        pre_firm += c / rate
        rate += f 

        new_estimate = pre_firm + x / rate 

        if ( estimate < new_estimate ):
            return "%.7f" % estimate

        estimate = new_estimate

    return ''

def main():
    for i in range(int(input())):

        (c,f,x) = map(float,raw_input().split())
        judge = do_calc(c,f,x)

        print('Case #%d: %s' % ( i+1, judge ))

if __name__ == '__main__':
    main()
