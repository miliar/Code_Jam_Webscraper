#!/usr/bin/env python
# -*- coding: utf-8 -*-

T = int(raw_input())

for case in xrange(1,T+1):

    N = int(raw_input())
    s = [ raw_input() for _ in xrange(N) ]
    res = 0

    f = [0]

    first = s[0]
    f[0] = first[0]

    for i in xrange(1,len(first)):
        if first[i] == first[i-1]:
            continue
        else:
            f.append(first[i])

    # print f
    count = [[] for _ in s]

    for i in xrange(N):
        ss = s[i]

        block = 0
        if f[block] != ss[block]:
            res = -1
            break

        j = 0
        c = 0
        while j < len(ss):
            if ss[j] != f[block]:
                if c == 0 or block+1 == len(f):
                    res = -1
                    break
                else:
                    count[i].append(c)
                    block += 1
                    c = 0
            else:
                c+=1
                j += 1
        count[i].append(c)

        # print count[i]

        if block < (len(f)-1):
            res = -1
            break

    # code
    print "Case #%d:" % case,
    if res < 0:
        print "Fegla Won"
    else:
        mean = [0 for _ in f]
        for i in xrange(N):
            assert len(count[i]) == len(f)
            for j in xrange(len(f)):
                mean[j] += count[i][j]/float(N)
        res = 0
        for i in xrange(N):
            for j in xrange(len(f)):
                res += abs(mean[j] - count[i][j])
        print int(res)
















