from collections import deque
# -*- coding: utf-8 -*-

if __name__=="__main__":
    T = int(raw_input())
    for test in xrange(T):
        R, k, N = raw_input().split()
        R, k, N = int(R), int(k), int(N)
        g = []
        g_input = raw_input().split()
        g.extend(g_input)
        euro = 0
        for run in xrange(R):
            g1 = []
            soma = 0 
            while True:
                elem = g.pop(0)
                g1.append(elem)
                soma = soma + int(elem)
                try:
                    if (soma + int(g[0])) > k:
                        break
                except Exception, e:
                    break

            g.extend(g1)
            euro = euro + soma   
        print "Case #%s: %s" % (test+1, euro)