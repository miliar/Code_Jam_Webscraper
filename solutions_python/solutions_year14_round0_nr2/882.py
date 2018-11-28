#!/usr/bin/env python
# -*- coding:utf-8 -*-
########################
# Google code jam
# Problem A. Magic Trick
# small input
# @Author yangdf
########################
import re
   # 123.123     456.456      789.789    

pattern = re.compile(r' +')

def getInput(line):
    '''get float value from input str
    '''
    line = line.strip()
    line = pattern.sub(' ', line)
    # print '*%s*' % line
    C, F, X = line.split(' ')
    # print '*'.join([C,F,X])
    return float(C), float(F), float(X)

if __name__ == '__main__':
    t = raw_input()
    for x in xrange(1, int(t)+1):
        speed = 2
        line = raw_input()
        C, F, X = getInput(line)
        count = 0
        extra_count = 0
        min_sum = X / speed
        while True:
            extra_count += C / speed
            speed = speed+F
            s = extra_count + X/speed
            if s > min_sum:
                break
            min_sum = s
        print 'Case #%d: %.7lf' % (x, min_sum)

        # print type(C)
        # print 'float:', C
        # print 'float:', F
        # print 'float:', X
