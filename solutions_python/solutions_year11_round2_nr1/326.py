#! /usr/bin/python2.6
# coding: utf-8

ntcase = int(raw_input())
for tcase in range(1, ntcase + 1):
    # read
    n = int(raw_input())
    lst = [raw_input() for _ in range(n)]
    
    # 'Every team plays at least two other teams.'
    # => denominator must not be zero.
    
    base = [[a.count('1'), len(a) - a.count('.')] for a in lst]
    wp = [a[0] / float(a[1]) for a in base]
    owp = [sum(sum(1 for k,ch in enumerate(lst[j]) if ch=='1' and k!=i) / float(base[j][1]-1) for j,ch in enumerate(lst[i]) if ch != '.' and j != i) / base[i][1] for i,a in enumerate(base)]
    oowp = [sum(owp[j] for j,ch in enumerate(lst[i]) if ch != '.') / base[i][1] for i,a in enumerate(base)]
    
    #print lst
    #print wp
    #print owp
    #print oowp

    # output
    print 'Case #%d:' % tcase
    for i in range(len(lst)):
        x = sum(map(lambda x,y: x*y, [0.25, 0.50, 0.25], [wp[i], owp[i], oowp[i]]))
        print '%.12f' % x
