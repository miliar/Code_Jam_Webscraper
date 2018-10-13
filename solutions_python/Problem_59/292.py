
"""
    This program is written by kawasaki, Japan.
    
    mail: kawasaki.yasuhiro@gmail.com
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
        '0 2',
        '/home/gcj/finals',
        '/home/gcj/quals',
        '2 1',
        '/chicken',
        '/chicken/egg',
        '/chicken',
        '1 3',
        '/a',
        '/a/b',
        '/a/c',
        '/b/b',
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

if DEBUG:
    import time
    _START_TIME = time.time()

#-------------------------------------------------------------------------------
#   Algorithm.

import os
import copy

T = int(readline())

qid = 1
while qid <= T:
    
    N, M = map(int, readline().split(' '))
    
    exist_path = []
    for i in xrange(N):
        exist_path.append(readline())
    
    new_path = []
    for i in xrange(M):
        new_path.append(readline())
    
    exist_folders = set()
    for path in exist_path:
        sp = filter(lambda x: len(x) > 0, [x for x in path.split('/')])
        if sp[0] == '/':
            sp = ['/' + sp[1]] + sp[2:]
        for i in xrange(1, len(sp) + 1):
            exist_folders.add('/'.join(sp[:i]))
    
    counter = 0
    new_folders = copy.deepcopy(exist_folders)
    for path in new_path:
        sp = filter(lambda x: len(x) > 0, [x for x in path.split('/')])
        if sp[0] == '/':
            sp = ['/' + sp[1]] + sp[2:]
        for i in xrange(1, len(sp) + 1):
            if '/'.join(sp[:i]) in new_folders:
                continue
            new_folders.add('/'.join(sp[:i]))
            counter += 1
    
    print 'Case #%d: %d' % (qid, counter)
    
    qid += 1

#---------------------------------------------------------------------------

if DEBUG:
    print '-' * 80
    print 'DEBUG version finished. %.3f [sec]' % (time.time() - _START_TIME)

