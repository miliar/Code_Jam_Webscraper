
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
        '3',
        '4 6 4',
        '1 4 2 1',
        '100 10 1',
        '1',
        '5 5 10',
        '2 4 2 3 4 2 1 2 1 3',
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
    
    R, k, N = map(int, readline().split(' '))
    g = map(int, readline().split(' '))
    
    head = 0
    earn = 0
    for i in xrange(R):
        total = 0
        start_head = head
        while total + g[head] <= k:
            total += g[head]
            head = (head + 1) % N
            if head == start_head:
                break
        earn += total
    
    print 'Case #%d: %d' % (qid, earn)
    
    qid += 1

#---------------------------------------------------------------------------

if DEBUG:
    print '-' * 80
    print 'DEBUG version finished.'

