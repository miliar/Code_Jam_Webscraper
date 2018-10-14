#!/usr/bin/python
# -*- coding:utf8 -*-

import sys

with open(sys.argv[1]) as f:
    T = f.readline().strip()
    for i in xrange(int(T)):
        mtx = []
        r, c = f.readline().strip().split(' ')
        for j in xrange(int(r)):
            cs = f.readline().strip().split(' ')
            mtx.append(cs)
        possible = True
        while True:
            minh = min(min(x) for x in mtx)
            #print 'min', minh
            pre_size = reduce(lambda x, y: x + y, [len(x) for x in mtx])
            #print 'pre', pre_size

            #remove row
            p = 0
            for j in xrange(len(mtx)):
                req = reduce(lambda x, y: x and y, map(lambda x: x == minh, mtx[p]))
                if req:
                    mtx.remove(mtx[p])
                    p = p - 1
                    #print mtx
                p = p + 1

            if len(mtx) == 0:
                break

            #remove column
            p = 0
            for j in xrange(len(mtx[0])):
                ceq = True
                for k in xrange(len(mtx)):
                    ceq = ceq and (mtx[k][p] == minh)
                if ceq:
                    for k in xrange(len(mtx)):
                        mtx[k].pop(p)
                    #print mtx
                    p = p - 1
                p = p + 1

            if len(mtx) == 0:
                break

            post_size = reduce(lambda x, y: x + y, [len(x) for x in mtx])
            #print 'post', post_size
            if pre_size == post_size:
                possible = False
                break
        if possible:
            print 'Case #' + str(i + 1) + ': YES'
        else:
            print 'Case #' + str(i + 1) + ': NO'
