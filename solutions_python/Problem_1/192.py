#!/usr/bin/python
''' Saving the Universe
Google Code Jam 2008
Qualification Round - Problem A
Grant Glouser <gglouser@gmail.com>
'''

import sys


def read_int_line(f):
    return int(f.readline().rstrip())

def read_search_engines(f):
    s = read_int_line(f)
    search_engines = []
    for i in range(s):
        search_engines.append(f.readline().rstrip())
    return search_engines

def read_queries(f):
    q = read_int_line(f)
    queries = []
    for i in range(q):
        queries.append(f.readline().rstrip())
    return queries

def build_matrix(search_engines, queries):
    matrix = []
    for engine in search_engines:
        d = []
        count = 0
        for q in queries:
            if engine == q:
                count = 0
            else:
                count += 1
            d.append(count)
        matrix.append(d)
    return matrix

def best_at(matrix, k):
    best = -1
    best_ix = -1
    for i in range(len(matrix)):
        if matrix[i][k] > best:
            best = matrix[i][k]
            best_ix = i
    return best_ix

def do_test_case(f, case_num):
    search_engines = read_search_engines(f)
    #print search_engines
    
    queries = read_queries(f)
    #print queries
    if len(queries) == 0:
        print 'Case #%d: 0' % (case_num + 1)
        return
    
    matrix = build_matrix(search_engines, queries)
    #for row in matrix:
    #    print row
    
    pos = len(queries) - 1
    switches = -1
    while pos > 0:
        best = best_at(matrix, pos)
        #print 'best at %d is %d ... stepping %d' % (pos, best, matrix[best][pos])
        pos -= matrix[best][pos]
        switches += 1
    if matrix[best][0] == 0:
        switches += 1
    print 'Case #%d: %d' % (case_num + 1, switches)

def main(input):
    f = file(input)
    n = read_int_line(f)
    for i in range(n):
        do_test_case(f, i)
    f.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: %s <input>' % sys.argv[0]
        sys.exit(1)
    main(sys.argv[1])
