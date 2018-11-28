#!/usr/bin/env python

import sys

sys.setrecursionlimit(1500)

def get_num_switches(s_engine, num_s_engines,query, num_query):
    cnt = 0
    if num_query == 0:
        return 0
    arr1 = []
    arr2 = []
    for p in range(num_s_engines):
        arr1.append(0)
        arr2.append(0)
    #get counts
    for i in range(num_query):
        for j in range(num_s_engines):
            if s_engine[j] == query[i]:
                arr1[j] = arr1[j] + 1
                if arr1[j] == 1:
                    #first time that SE appears
                    arr2[j] = i
                continue
    #find SE with latest appearance
    mx = max(arr2)
    mx_index = arr2.index(mx)
    #If a search engine is not in the query, then its over
    if (min(arr1) == 0):
        return 0
    
    return 1 + get_num_switches(s_engine, num_s_engines, query[mx:], num_query - mx)
    #return cnt


def main():
    
    f = file("A-large.in", "r")
    of = file("output.out", "w")
    
    num_cases = f.readline()

    for i in range(int(num_cases)):
        s_engine = []
        query = []
        num_s_engines = int(f.readline())
        #print "Num Engines: %d" % num_s_engines
        for j in range (num_s_engines):
            s_engine.append( f.readline())
        #    print "S Engines: %s" % s_engine[-1]
        
        num_query = int(f.readline())
        #print "Num Queries: %d" % num_query
        if num_query > 0:
            for k in range (num_query):
                query.append(f.readline())
         #       print "Query: %s" % query[-1]
            
        cnt = get_num_switches(s_engine, num_s_engines,query, num_query)    
        
        
        of.write("Case #%d: %d\n" % ((i+1),cnt))
        print "Case #%d: %s" % ((i+1),cnt)
        