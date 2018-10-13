#! /usr/bin/python
"""
Google code jam 2008
  Qualification Round
  A. Saving the Universe

Ramsey Nasser
  http://ramseynasser.com/
  ramsey@ramseynasser.com

The next engine to use is always the one that is further down in the queries
list. All queries up to that engine's name are consumed, and the process
repeats until the query list is empty. Optimal, no?
"""

import sys

inlist = [line.strip() for line in open(sys.argv[1])]

N = int(inlist.pop(0))

# Handle a test case
for i in range(N):
    switches = 0
    queries = []
    engines = []
    
    # Parse engines
    S = int(inlist.pop(0))
    engines = inlist[:S]
    inlist = inlist[S:]
    
    # Parse queries
    Q = int(inlist.pop(0))
    queries = inlist[:Q]
    inlist = inlist[Q:]
    
    # Always use the engine that is further down the query list
    while True:
        max_index = 0
        next_engine = None
        for engine in engines:
            if engine not in queries:
                next_engine = engine
                max_index = len(queries)
                break
            else:
                index = queries.index(engine)
                if index > max_index:
                    max_index = index
                    next_engine = engine
                    
        queries = queries[max_index:]
        if len(queries) == 0: break
        else: switches += 1
    print "Case #%d: %d"%(i+1, switches)