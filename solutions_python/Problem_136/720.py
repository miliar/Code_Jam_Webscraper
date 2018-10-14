#/usr/bin/env python2.7
#-*- coding:utf-8 -*-
#huanghaiping2@gmail.com

import sys

def readline():
    return sys.stdin.readline()

if __name__ == '__main__':
    T = int(readline())
    for i in xrange(T):
        print "Case #%s:" % (i+1),
        C, F, X = [float(i) for i in readline().split(' ')]
        FarmTime = []
        FarmTime.append(0.0)
        TotalTime = []
        TotalTime.append(X/2.0)
        j = 1
        #print 'new total time (with 0 farm):%s' % (TotalTime[0])
        while True:
            t = (C/(2+(j-1)*F)) + FarmTime[j-1]
            FarmTime.append(t)
            #print 'new farm time (with %s farm):%s' % (j, t)
            newTime = FarmTime[j] + X/(2+j*F)
            #print 'new total time (with %s farm):%s' % (j, newTime)
            TotalTime.append(newTime)
            lastTime = TotalTime[j-1]
            if lastTime <= newTime:
                print "%.7f" % lastTime
                break
            j += 1

