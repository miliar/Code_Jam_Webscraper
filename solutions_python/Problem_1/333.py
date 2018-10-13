#!/usr/bin/env python
'''
CodeJam 2008
Saving the Universe
2008-07-17
Marc Garcia <garcia.marc@gmail.com>
'''
import sys

def readfile(filename):
    f = open(filename, 'rb')

    data = []
    num_cases = f.readline()
    for case in xrange(int(num_cases)):
        num_engines = f.readline()
        engines = []
        for engine in xrange(int(num_engines)):
            engines.append(f.readline()[:-1])
        num_queries = f.readline()
        queries = []
        for query in xrange(int(num_queries)):
            queries.append(f.readline()[:-1])
        data.append(dict(engines=engines, queries=queries))
    return data

def calculate(data):
    def next_switch(queries):
        result = 0 ; found_engines = set()
        for cnt, query in enumerate(queries):
            found_engines.add(query)
            if len(found_engines) >= len(engines):
                current_engine = query
                found_engines = set()
                result = next_switch(queries[cnt:])
                return result + 1
        return 0

    for case_num, case_data in enumerate(data):
        engines = case_data['engines'] ; queries = case_data['queries']
        result = next_switch(queries)

        print 'Case #%s: %s' % (case_num + 1, result)
        
if __name__ == '__main__':
    sys.setrecursionlimit(1100)
    calculate(readfile('A-large.in'))

