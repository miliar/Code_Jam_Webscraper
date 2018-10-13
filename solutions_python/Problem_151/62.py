#!/usr/bin/python

import sys

f = sys.stdin

tt = eval(f.readline().strip())

m1 = m2 = 0
ss = []
cont = []
m = 0
n = 0

def dfs(i):
    global ss, cont, m, n, m1, m2
    if i == m:
        tmp = 0
        for j in range(0, n):
            ll = len(cont[j])
            if ll == 0:
                return
            tmp1 = 1
            for k in range(0, ll):
                s = 0
                for r in range(0, k):
                    def comm(st1, st2):
                        if len(st1) < len(st2):
                            l = len(st1)
                        else:
                            l = len(st2)
                        i = 0
                        while i < l:
                            if st1[i] != st2[i]:
                                break
                            i += 1
                        return i
                    h = comm(cont[j][k], cont[j][r])
                    if h > s:
                        s = h
                tmp1 += len(cont[j][k]) - s
            tmp += tmp1
        if tmp > m1:
            m1 = tmp
            m2 = 1
        elif tmp == m1:
            m2 += 1
        return 

    for j in range(0, n):
        cont[j].append(ss[i])
        dfs(i + 1)
        cont[j].pop()
        #if len(cont[j]) == 0:
        #    break

for cc in range(1, tt + 1):
    tmp = f.readline()
    tmp = tmp.split()
    m = eval(tmp[0])
    n = eval(tmp[1])
    ss = []
    for i in range(0, m):
        tmp = f.readline()
        tmp = tmp.strip()
        ss.append(tmp)
    m1 = m2 = 0
    cont = []
    for i in range(0, n):
        cont.append([])
    dfs(0)
    print "Case #%d: %d %d" % (cc, m1, m2)
