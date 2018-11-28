#! /usr/bin/python2.6
# coding: utf-8
#isdebug = True
isdebug = False
import collections

ntcases = int(raw_input())
for tcase in range(1, ntcases+1):
    # read
    line = raw_input().split()
    C = int(line[0])
    D = int(line[C+1])
    N = int(line[C+1+D+1])
    
    combine = line[1  :1+C]
    opposed = line[2+C:2+C+D]
    elemlst = line[-1]
    
    # normalize
    oo = {}
    for e1,e2,c in combine:
        oo[(e1, e2)] = c
        oo[(e2, e1)] = c
    combine = oo
    
    oo = collections.defaultdict(list)
    for e1,e2 in opposed:
        oo[e1].append(e2)
        oo[e2].append(e1)
    opposed = oo
    
    if isdebug:
        #print 'C:',C
        #print 'D:',D
        #print 'N:',N
        print 'combine:',combine
        print 'opposed:',opposed
        print 'elemlst:',elemlst

    # calc
    lst = []
    for elem in elemlst:
        lst.append(elem)
        
        # check: combine relation is exists
        if len(lst) < 2:
            continue
        key = (lst[-2], lst[-1])
        if len(lst) > 1 and combine.has_key(key):
            if isdebug:
                print 'combine* %s -> %s' % (lst, lst[:-2] + [combine[key]])
            lst[-2:] = [combine[key]]
        
        # check: opposed relation is exists
        if len(lst) < 2:
            continue
        olst = opposed[lst[-1]]
        for i in xrange(len(lst) - 1, -1, -1):
            if lst[i] in olst:
                if isdebug:
                    print 'opposed* %s -> []' % (lst)
                lst = []
                break
        
    # result
    print 'Case #%d:' % tcase, '[%s]' % ', '.join(lst)
    if isdebug:
        print ''

