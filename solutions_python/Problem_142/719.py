# -*- coding: utf-8 -*-
"""
Created on Sat May 03 17:11:56 2014

@author: Ennassiri
"""
from collections import OrderedDict
import numpy as np
import networkx as nx
from itertools import groupby
import itertools


f = open( "test2.in", "r" )
out = open( "result.out", "w")
T = int(f.readline())

def myformat(string1):
    return [len(list(group)) for key, group in groupby(list(string1))]
    
    
def number_operations(string1,string2):
    if string1 == string2 :
        return 0
    else :
        if (string1 in string2) or (string2 in string1):
            return abs(len(string2) - len(string1))
        else :
            table1 = myformat(string1)
            table2 = myformat(string2)
            print len(table1)
            print len(table2)
            c=[abs(table1[i]-table2[i]) for i in range(len(table1))]
            return sum(c)

def diffradical(strings):    
    s = 0
    radical = str(''.join(ch for ch, _ in itertools.groupby(strings[0])))
    for i in strings:
        s = s + abs(len(i)-len(radical))
    return s
    
def strsol(strings):
    M = np.zeros([len(strings),len(strings)])
    for i in range(len(strings)) :
        for j in range(len(strings)):
            if str(''.join(ch for ch, _ in itertools.groupby(strings[i]))) != str(''.join(ch for ch, _ in itertools.groupby(strings[j]))):          
                return "Fegla Won"
                
            else :
                print strings[i]
                print strings[j]
                print str("".join(OrderedDict.fromkeys(strings[i])))
                M[i,j] = number_operations(strings[i],strings[j])
    G = nx.from_numpy_matrix(M)
    T = nx.minimum_spanning_tree(G)
    return min(diffradical(strings),int(T.size(weight='weight')))

for n in xrange(1,T+1):
    N = int(f.readline())
    strings = ["" for x in range(N)]

    for i in range(N):
        strings[i] = str(f.readline()).strip()
        
    solution = strsol(strings)
    print solution
    # Problem solution
    out.write("Case #%d: %s\n" % (n, str(solution)))

f.close()
out.close()