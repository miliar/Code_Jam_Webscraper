
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
        '4',
        '3 26000000 11000000 6000000',
        '3 1 10 11',
        '2 800000000000000000001 900000000000000000001',
        '3 11612 9337 9338',
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

C = int(readline())

qid = 1
while qid <= C:
    
    N, t = readline().split(' ', 1)
    N = int(N)
    t = map(int, t.split(' '))
    
    def gcd(a, b):
        assert 0 < a and 0 < b
        
        r = a % b
        while r > 0:
            a, b = b, r
            r = a % b
        return b
    
    t_set = set(t)
    t = [x for x in t_set]
    sub = [abs(t[i + 1] - t[i]) for i in xrange(len(t) - 1)]
    while True:
        sub.sort()
        if len(sub) == 1:
            break
        
        if sub[1] % sub[0] == 0:
            break
        sub = [gcd(sub[i], sub[i + 1]) for i in xrange(len(set(sub)) - 1)]
    
    if t[0] % sub[0] != 0:
        answer = (t[0] / sub[0] + 1) * sub[0] - t[0]
    else:
        answer = 0
    
    print 'Case #%d: %d' % (qid, answer)
    
    qid += 1

#---------------------------------------------------------------------------

if DEBUG:
    print '-' * 80
    print 'DEBUG version finished.'

