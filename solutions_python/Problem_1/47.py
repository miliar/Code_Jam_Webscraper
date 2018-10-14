#!/usr/bin/env python

from sys import *

def unique(queries):
    list = []
    prev = None
    for q in queries:
        if q != prev:
            list.append(q)
            prev = q
            
    return list

def countSwitches(engines, queries):
    #print "======== New pass"
    queries = unique(queries)
    use = None    
    weighted = []
    switches = 0
    
    #print queries
    #print "Engine: ", engine
    
    for e in engines:
        try:
            idx = queries.index(e)
            weighted.append((e, idx))
        except ValueError:
            use = e
            
    if use != None:
        return 0    #We found engine not presented in the query list
    else:
        weighted.sort(lambda x,y:cmp(x[1],y[1]))
        #print weighted
        
        (e, idx) = weighted.pop()
        #while e == engine:
        #    (e, idx) = weighted.pop()    
        
        if idx < len(queries):
            switches = 1 + countSwitches(engines, queries[idx:])
        else:
            return 1      
            
    return switches

def processCase(engines, queries, case):
    #print engines    
    switches = countSwitches(engines, queries)    
    print "Case #%d: %d" % (case, switches)
    
    return

def process(lines):
    n = int (lines[0])
    case = 1
    i = 1
    while case <= n:
        s = int (lines[i])
        i += 1
        
        engines = []
        while s > 0:
            engines.append(lines[i].strip("\r\n"))
            i += 1
            s -= 1
        
        q = int (lines[i])
        i += 1
            
        queries = []
        while q > 0:
            queries.append(lines[i].strip("\r\n"))
            i += 1
            q -= 1
            
        processCase(engines, queries, case)
        case += 1
        

def usage():
    print "Usage %s input" % argv[0]

def main():
    setrecursionlimit(2048)
    
    if len(argv) < 2:
        usage()
        exit()
        
    input = argv[1]
    f = open(input, 'r')
    
    try:
        lines = f.readlines()
        process(lines)
        
    finally:
        f.close()

if __name__ == '__main__':
    main()