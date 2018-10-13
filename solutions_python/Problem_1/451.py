#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nycholas de Oliveira e Oliveira <nycholas@gmail.com>

def get_engine(lst_engine, lst_query):
    max_query = {}
    for engine in lst_engine:
        max_query[engine] = 0
        for query in lst_query:
            if engine == query:
                break
            else:
                max_query[engine] = max_query[engine] + 1
    return sorted(max_query, key=max_query.__getitem__, reverse=True)

nro_case = int(raw_input())
for case in range(nro_case):
    nro_engine = int(raw_input())
    lst_engine = []
    for engine in range(nro_engine):
        lst_engine.append(raw_input())
    nro_query = int(raw_input())
    lst_query = []
    for query in range(nro_query):
        lst_query.append(raw_input())
    switch = 0
    index = 0   
    best_engine = get_engine(lst_engine, lst_query)[0]
    for query in lst_query:
        if best_engine == query:
            switch = switch + 1
            best_engine = get_engine(lst_engine, lst_query[index:])[0]
        index = index + 1               
    print "Case #%d: %d" % (case + 1, switch)

