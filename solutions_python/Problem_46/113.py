import sys
import re
from itertools import *
import copy
from heapq import *

INFINITE = 100000000+1

class _Matrix(object):
    def __init__(self, values, rows, cols, default):
        self.rows = rows
        self.columns = cols
        self.array = values
        self.default = default
    def get(self, r, c):
        if r not in self.array or c not in self.array[r]: return self.default
        return self.array[r][c]
    def set(self, r, c, value):
        self.array[r][c] = value
    def __iter__(self):
        return iter(self.array)
    def for_each(self, callback_func):
        for r in xrange(self.rows):
            for c in xrange(self.columns):
                callback_func(r, c, self.get(r,c))
    def __repr__(self):
        return '\n'.join(' '.join(str(self.get(r, c)) for c in xrange(self.columns)) for r in xrange(self.rows))

def Matrix(values, rows, cols, default):
    d = dict()
    for r, row in itertools.izip(itertools.count(0), values):
        rowdict = dict()
        d[r] = rowdict
        for c, value in itertools.izip(itertools.count(0), row):
            rowdict[c] = value
    return _Matrix(d, rows, cols, default)

def Matrix2(rows, cols, initial):
    d = dict()
    for r in xrange(rows):
        rowdict = dict()
        d[r] = rowdict
        for c in xrange(cols):
            rowdict[c] = initial
    return _Matrix(d, rows, cols, initial)

def copy_matrix(m):
    return _Matrix(copy.deepcopy(m.array), m.rows, m.columns, m.default)

def find_min(total_est, vals):
    cur_min = 1000000
    cur = None
    for val in vals:
        x = total_est[val]
        if x < cur_min:
            cur = val
            cur_min = x
    return cur

def swaplines(node, line):
    ret = []
    for x in xrange(len(node)):
        if x == line:
            ret.append(node[line+1])
        elif x == line+1:
            ret.append(node[line])
        else:
            ret.append(node[x])
    return tuple(ret)

def cur_expand(node):
    rows = len(node)
    for r in xrange(rows-1):
        yield swaplines(node, r)

def cur_endcondition(node):
    for line, c in izip(node, count(1)):
        if line.find('1', c) != -1:
            return False
    return True

def cur_heuristic(node):
    ret = 0
    for line, c in izip(node, count(1)):
        x = line.rfind('1', c)
        ret +=  x - c if x != -1 else 0
    return ret

def AStar(start, expand, endcondition, heuristic):
    #print start
    nodes_visited = set()
    nodes_eval    = set()
    heap = [(0, start)]
    hval = heuristic(start)
    nodes_eval.add(start)
    #print endcondition(start)
    #print hval
    optimal = dict()
    heurist = dict()
    total_est = dict()
    optimal[start] = 0
    heurist[start] = hval
    total_est[start] = hval
    while len(nodes_eval):
#        print len(nodes_eval)
        #cur = find_min(total_est, nodes_eval)
        cur = heappop(heap)
        #print cur, total_est[cur]
        #nodes_eval.remove(cur)
        node = cur[1]
        if endcondition(node):
            return optimal[node]
        nodes_visited.add(node)
        for neighbor in expand(node):
            if neighbor in nodes_visited:
                continue
            possible_opt = optimal[node] + 1
            hval = heuristic(neighbor)
            if neighbor not in nodes_eval:
                nodes_eval.add(neighbor)
                heappush(heap, (hval + possible_opt, neighbor))
                use_possible = True
            elif possible_opt < optimal[neighbor]:
                use_possible = True
            else:
                use_possible = False
            if use_possible:
                optimal[neighbor] = possible_opt
                heurist[neighbor] = hval
                total_est[neighbor] = possible_opt + hval
                


def put_output(out, number, count):
    out.write('Case #%d: %d\n' % (number, count))
    out.flush()

def run(infile, outfile):
    input = open(infile, 'r')
    lines = input.readlines()
    input.close()
    outfile = open(outfile, 'w')
    first = lines.pop(0).strip()
    num = int(first)
    for i in xrange(num):
        #print i
        n = int(lines.pop(0).strip())
        print n,
        mat = []
        for j in xrange(n):
            mat.append(lines.pop(0).strip())
        mat = tuple(mat)
        v = AStar(mat, cur_expand, cur_endcondition, cur_heuristic)
        print i+1, v
        #print v
        put_output(outfile, i+1, v)
        outfile.flush()
    outfile.close()
if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])
    #test_run()
    #pass

