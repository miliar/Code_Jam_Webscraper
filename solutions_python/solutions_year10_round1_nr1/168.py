# -*- coding: utf-8 -*-

t = int(raw_input())

for case in xrange(t):
    n, k = [int(inputs) for inputs in raw_input().split(' ')]
    
    dots = ''.join(['.' for inputs in xrange(n)])
    dotslen = len(dots)
    rletters = ''.join(['R' for inputs in xrange(k)])
    bletters = ''.join(['B' for inputs in xrange(k)])
    
    lines = []
    columns = []
    d1 = {}
    d2 = {}
    
    rwins = False
    bwins = False
    
    for i in xrange(n):
        line = raw_input().replace('.', '')
        line = dots[:dotslen - len(line)] + line
        lines.append(line)
        for j, c in enumerate(line):
            if i == 0: columns.append(c)
            else: columns[j] += c
            
            d1i = (j + 1) - (i + 1)
            if d1i in d1: d1[d1i] += c
            else: d1[d1i] = c
            
            d2i = (n - j) - (i + 1)
            if d2i in d2: d2[d2i] += c
            else: d2[d2i] = c
     
    for i in xrange(n):
        rwins = rwins or (rletters in lines[i] or rletters in columns[i])
        bwins = bwins or (bletters in lines[i] or bletters in columns[i])
        if rwins and bwins: break
    
    if not rwins or not bwins:
        d1 = d1.values()
        d2 = d2.values()
        for i in xrange(len(d1)):
            rwins = rwins or (rletters in d1[i] or rletters in d2[i])
            bwins = bwins or (bletters in d1[i] or bletters in d2[i])
            if rwins and bwins: break
    
    if rwins and bwins:
        result = 'Both'
    elif rwins:
        result = 'Red'
    elif bwins:
        result = 'Blue'
    else:
        result = 'Neither'
    
    print 'Case #%d: %s' % (case + 1, result)
