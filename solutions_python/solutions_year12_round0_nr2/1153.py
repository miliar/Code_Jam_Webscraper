#!/usr/bin/env python
import math

fh = file('input.txt', 'r')
t = fh.readline()
t = t.replace('\n', '')
print t
t = int(t)

out = file('out.txt', 'w')


for case in range(0, t):
    line = fh.readline()
    line = line.replace('\n', '')
    line = line.split(' ')
    N = int(line[0])
    S = int(line[1])
    P = int(line[2])
    scores = line[3:]
    res = 0
    for ti in scores:
        ti = int(ti)
        if ti >= P * 3:
            res = res + 1
        else:
            avg = (ti - P) / 2.0
            
            if avg >= 0:
                tf = math.floor(avg)
                #print tf
                if P <= tf + 1:
                    res = res + 1
                elif P <= tf + 2 and S > 0:
                    S = S-1
                    res = res + 1

    print 'Case #%d: %d' % (case+1, res)
    out.write('Case #%d: %d\n' % (case+1, res))
    

out.close()
fh.close()

#
#N = 3
#S = 0
#P = 8
#scores = [23, 22, 21]
#
#res = 0
#for ti in scores:
#    if ti >= P * 3:
#        res = res + 1
#    else:
#        avg = (ti - P) / 2.0
#        if avg >= 0:        
#            tf = math.floor(avg)
#            print tf
#            if P <= tf + 1:
#                res = res + 1
#            elif P <= tf + 2 and S > 0:
#                S = S-1
#                res = res + 1
#
#print res
