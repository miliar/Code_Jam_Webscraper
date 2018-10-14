import sys
in_file = file(sys.argv[1], 'r')
out_file = file('test_big.out', 'w')

num_cases = int(in_file.readline())

for case in range(1, num_cases + 1):
    num_engines = int(in_file.readline())
    engines = [in_file.readline()[:-1] for i in range(num_engines)]
    
    num_queries = int(in_file.readline())
    queries = [in_file.readline()[:-1] for i in range(num_queries)]
    
    num_switches = -1
    cur_engine = None
    while queries:
        num_switches += 1
        #Check that all of the engines are left in the queries
        present = [e in queries for e in engines if e != cur_engine]
        if not all(present):
            break
        
        next = max(queries.index(e) for e in engines if e != cur_engine)
        cur_engine = queries[next]
        queries = queries[next:]
        queries.pop(0)
    else:
        #Need this if we actually pop the last entry...because if we do, we
        #Have neglected to count the final switch
        num_switches += 1

    #Special case for no queries
    if num_switches < 0: num_switches = 0
    
    print 'Case #%d: %d' % (case, num_switches)
    out_file.write('Case #%d: %d\n' % (case, num_switches))

out_file.close()
