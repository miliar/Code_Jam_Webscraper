#!/usr/bin/python


def parse(f):
    lines = f.readlines()
    index = 0
    case = []
    line = lines[0].strip()
    N = int(line)
    index = 1
    cases = []
    for i in range(N):
        line = lines[index].strip()
        S = int(line)
        search_engines = []
        for j in range(S):
            index += 1 
            line = lines[index].strip()
            search_engines.append(line)
        index += 1 
        line = lines[index].strip()
        Q = int(line)
        queries = []
        for k in range(Q):
            index += 1 
            line = lines[index].strip()
            queries.append(line)
        d = {}
        d['search_engines'] = search_engines
        d['queries'] = queries
        cases.append(d)
        index += 1
    return cases


f = open('test.txt','r')

cases = parse(f)


def solve(case):
    search_engines = case['search_engines']
    queries = case['queries']
    steps = {}
    for s in search_engines:
        steps[s] = -1

    count = 0
    switch_count = 0
    switch_chance = len(search_engines)
    for q in queries:
        print 'query:', q
        count += 1
        if steps.has_key(q):
            if steps[q] == -1:
                steps[q] = count
                switch_chance -= 1
        if switch_chance == 0:
            print 'switch'
            switch_count += 1
            for s in search_engines:
                steps[s] = -1
            switch_chance = len(search_engines) - 1
            steps[q] = count

    return switch_count

o = open('output.txt','w')
case_number = 1
for case in cases:
    o.write('Case #%s: %s\n' % (case_number, solve(case)))
    case_number += 1
