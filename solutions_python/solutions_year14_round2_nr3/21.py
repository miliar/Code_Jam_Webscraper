import pdb
import sys
import re
import time
from collections import defaultdict
from itertools import *
from copy import copy, deepcopy
from pprint import pprint
from glob import glob

taskname = 'C'
input = None

def readstr():
    return next(input).strip()

def readintlist():
    lst = map(int, readstr().split())
    return lst

def readint():
    lst = readintlist()
    assert len(lst) == 1
    return lst[0]

def run_wave(edges, visited, front):
    while front:
        node = front.pop()
        if node in visited:
            continue
        visited.add(node)
        front.extend(edges[node])
    return visited


def try_backtrack(edges, visited, path, nodes_of_interest, target_node):
#    print 'trybacktrack:', path, target_node
    nodes_of_interest = nodes_of_interest.copy()
    path = path[:]
    while True:
        node, reachable = path.pop()
        neighbours = edges[node]
#        print '   ', node, neighbours, reachable
        if target_node in neighbours:
            still_reachable = run_wave(edges, visited.copy(), list(reachable))
            nodes_of_interest -= visited
            if nodes_of_interest.issubset(still_reachable):
                return path, node, reachable - visited
            else:
                return None, None, None
        else:
            nodes_of_interest |= neighbours
     

def solvecase():
    node_count, edge_count = readintlist()
    zips = [readstr() for _ in xrange(0, node_count)]  
    edges = defaultdict(set)
    for _ in xrange(edge_count):
        a, b = readintlist()
        edges[a - 1].add(b - 1)
        edges[b - 1].add(a - 1)
        
    current_node = min((i for i in xrange(node_count)), key=zips.__getitem__)
    visited = set([current_node])
    result = zips[current_node]
    path = []
    reachable = set()
    while len(visited) < len(zips):
        neighbours = edges[current_node] - visited
        reachable |= neighbours
#        print current_node, neighbours, reachable, visited 
        for next_node in sorted(reachable, key=zips.__getitem__):
            if next_node not in neighbours:
                tmp_path, tmp_current_node, tmp_reachable = try_backtrack(edges, visited, path, neighbours, next_node)
                if tmp_path is None:
                    continue
                path = tmp_path
                reachable = tmp_reachable
                current_node = tmp_current_node
            # else just go there
            path.append((current_node, reachable.copy()))
            current_node = next_node
            result += zips[current_node]
            reachable.remove(current_node)
            visited.add(current_node)
            break
        else:
            assert False
    return result

def solve(input_name, output_name):
    global input
    tstart = time.clock()
    input = open(input_name, 'r')
    output = open(output_name, 'w')
    casecount = readint()
    
    for case in range(1, casecount + 1):
        s = solvecase()
        s = "Case #%d: %s" % (case, str(s)) 
        print >>output, s
        print s 
        
    input.close()
    output.close()
    print '%s solved in %.3f' % (input_name, time.clock() - tstart)

def main():
    input_names = glob(taskname + '-*.in')
    assert len(input_names)
    input_names.sort(reverse = True)
    for input_name in input_names:
        solve(input_name, input_name.replace('.in', '.out')) 
                
if __name__ == '__main__':
    main()
