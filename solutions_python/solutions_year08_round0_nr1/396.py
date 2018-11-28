#!/usr/bin/python



f = open('A-small.in')


test_cases = int(f.readline().strip())

case_num = 1

for i in range(test_cases):
    search_engines = []
    queries = []
    switches = 0
    se = int(f.readline().strip())
    for j in range(se):
        search_engines.append(f.readline().strip()) 

    qs = int(f.readline().strip())

    for j in range(qs):
        queries.append(f.readline().strip())
#    conflicts = [ x for x in search_engines if x not in queries ]
#    print conflicts
#    if conflicts:
#        print "Case #%d: 0" % (case_num,)
#        continue
    queue = search_engines[:]
    for q in queries:
        if q in queue:
            queue.remove(q)
        if len(queue) == 0:
            switches += 1
            queue = search_engines[:]
            queue.remove(q)
    print "Case #%d: %d" % (case_num, switches)
    case_num += 1
