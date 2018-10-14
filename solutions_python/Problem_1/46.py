#!/usr/bin/env python
#-*- coding:utf-8 -*-

def switches(engines, queries):
    explored = [[0]]
    while True:
        last = explored[-1]
        new = {}
        for position in last:
            for engine in engines:
                end = True
                for i, query in enumerate(queries[position:]):
                    if query == engine:
                        end = False
                        if engine not in new or new[engine] < i+position:
                            new[engine] = i+position
                        break
                if end == True:
                    return len(explored) - 1
        
        explored.append(new.values())

if __name__ == '__main__':
    from sys import argv, exit
    if len(argv) < 2:
        test()
        exit()
    
    file_name = argv[1]
    lines = open(file_name).read().split('\n')[0:-1]
    nb_inputs = int(lines[0])
    line_no = 0
    lines = lines[1:]
    
    for n in range(nb_inputs):
        line = lines[line_no]
        line_no += 1
        nb_search_engines = int(line)
        search_engines = []
        for i in range(nb_search_engines):
            search_engines.append(lines[line_no+i])
        line_no += nb_search_engines
        
        line = lines[line_no]
        line_no += 1
        nb_queries = int(line)
        queries = []
        for i in range(nb_queries):
            queries.append(lines[line_no+i])
        line_no += nb_queries
        print 'Case #%s:' % (n+1), switches(search_engines, queries)

