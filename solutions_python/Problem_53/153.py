
"""
    This program is written by kawasaki, Japan.
    
    mail: kawasaki-yasuhiro@gmail.com
    twitter: http://twitter.com/pheromo/
    blog: http://d.hatena.ne.jp/phero/
    
    copyright 2010 kawasaki.
"""

#DEBUG = True
DEBUG = False

import sys

if DEBUG:
    input_data = [
        '5',
        '1 0',
        '1 1',
        '4 0',
        '4 47',
        '4 71',
    ]
else:
    input_data = []
    for line in sys.stdin:
        while line[-1] in ['\r', '\n']:
            line = line[:-1]
        input_data.append(line)

line_id = 0
def readline():
    global line_id
    line_id += 1
    return input_data[line_id - 1]

#-------------------------------------------------------------------------------
#   Algorithm.

T = int(readline())

qid = 1
while qid <= T:
    
    N, K = map(int, readline().split(' '))
    
    if K == 0:
        state = 'OFF'
    else:
        all_on_bit = 2 ** N - 1
        if K & all_on_bit == all_on_bit:
            state = 'ON'
        else:
            state = 'OFF'
    
    print 'Case #%d: %s' % (qid, state)
    
    qid += 1

#---------------------------------------------------------------------------

if DEBUG:
    print '-' * 80
    print 'DEBUG version finished.'

