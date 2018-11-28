#!/usr/bin/python

def mostdistant(engine, engines, queries):
    #print "currentengine: %s" % engine
    _engines = {}
    for e in engines:
        _engines[e] = True
 #   if engine in _engines:
 #       del _engines[engine]
    consumed = 0

    #print _engines
    for query in queries:
        if query in _engines:
            del _engines[query]
            if len(_engines) == 0:
                return consumed, query
                if consumed == 0:
                    print "waaa"
                    exit()
                break
        #print "removing %s from possible engines" % query
        consumed += 1
    newengine = _engines.keys()[0]
    return consumed, newengine

f = open("input")
numcases = int(f.readline())


for case in range(1,numcases+1):
    numengines = int(f.readline())
    engines = [f.readline().strip() for i in range(0,numengines)]
    numqueries = int(f.readline())
    queries = [f.readline().strip() for i in range(0,numqueries)]

    consumed, curengine = mostdistant(None, engines, queries)
    switches = 0
    while consumed < len(queries):
        #print consumed
        c,e = mostdistant(curengine, engines, queries[consumed:])
        #print "Engine: %s, queries: %s" % (e, c)
        consumed += c
        switches += 1
    print "Case #%s: %s" % (case, switches)


