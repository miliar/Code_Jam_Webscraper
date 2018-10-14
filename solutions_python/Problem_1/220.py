#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    n = int(raw_input())
    for i in range(n):
        ns = int(raw_input())
        se = []
        a = {}
        for j in range(ns):
            se.append(raw_input())
            a['%s' % se[-1]] = []
        nq = int(raw_input())
        queries = []
        for j in range(nq):
           queries.append(raw_input())
        
        s = 0
        for j in range(nq):
            for engine in se:
                if queries[j] == engine:
                    a[engine].append(0)
                else:
                    a[engine].append(1)

        start = 0
        while True:
            if start == nq:
                break
            b = {}
            Max = []
            for engine in se:
                for j in range(start, nq):
                    if a[engine][j] == 0:
                        break
                    else:
                        if b.has_key(engine):
                            b[engine] += 1
                        else:
                            b[engine] = 1
                            
                        if len(Max) == 0:
                            Max = [engine, b[engine]]
                        else:
                            if b[engine] > Max[1]:
                                Max = [engine, b[engine]]
            start += Max[1]
            if start == nq:
                break
            else:
                s += 1
            
        print "Case #%d: %d" % (i+1, s) 

if __name__ == '__main__':
    main()
