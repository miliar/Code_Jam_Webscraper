#!/usr/bin/env python
#coding:utf-8
#py 2
T = int(raw_input().strip()) #1 100
for cas in xrange(1, T + 1):
    #N 1 1e3 K 1 N
    N, K = map(int, raw_input().strip().split())
    a = [0 for i in xrange(N + 2)]
    a[0] = 1
    a[N + 1] = 1
    res_y, res_z = -1, -1
    best_pos = -1
    for i in xrange(K):
        l = -1
        best_pos = -1 #clear state
        for j in xrange(N + 2):
            if a[j] == 0:
                if l == -1:
                    l = j
            else:
                if l != -1:
                    #end of gaps
                    r = j - 1
                    mid = (l + r)/2
                    ls, rs = mid - l, r - mid
                    y, z = max(ls, rs), min(ls, rs)
                    replace = False
                    if best_pos == -1:
                        replace = True
                    else:
                        if z > res_z:
                            replace = True
                        elif z == res_z:
                            if y > res_y:
                                replace = True
                            elif y == res_y:
                                if mid < best_pos:
                                    replace = True
                    if replace:
                        best_pos, res_y, res_z = mid, y, z
                    l = -1
        a[best_pos] = 1 #K <= N, at least one position
    print "Case #%d: %d %d" % (cas, res_y, res_z)
