#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2014 george 
#
# Distributed under terms of the MIT license.
from cStringIO import StringIO

def process(data):
    lin1 = int(data[0])
    data1 = set(data[1:5][lin1-1].split())
    lin2 = int(data[5])
    data2 = set(data[6:][lin2-1].split())
    result =  data1.intersection(data2)

    if len(result) == 1:
        return result.pop()
    elif len(result) == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'



if __name__ == '__main__':
    data = '''
    3
    2
    1 2 3 4
    5 6 7 8
    9 10 11 12
    13 14 15 16
    3
    1 2 5 4
    3 11 6 15
    9 10 7 12
    13 14 8 16
    2
    1 2 3 4
    5 6 7 8
    9 10 11 12
    13 14 15 16
    2
    1 2 3 4
    5 6 7 8
    9 10 11 12
    13 14 15 16
    2
    1 2 3 4
    5 6 7 8
    9 10 11 12
    13 14 15 16
    3
    1 2 3 4
    5 6 7 8
    9 10 11 12
    13 14 15 16
    '''
    data = open('/tmp/in', 'r+').read()

    data = data.strip().split('\n')
    total = int(data[0])
    data = data[1:]

    for i in xrange(1, total+1):
        current = data[:10]
        data = data[10:]
        print "Case #{}: {}".format(i, process(current))

