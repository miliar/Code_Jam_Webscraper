import sys

def read_file(file_name):
    lines = []
    for line in open(file_name):
        lines.append(line.strip())
    lines.reverse()
    cases = int(lines.pop())
    while lines:
        search_engine_no = int(lines.pop())
        count = 0
        search_engines = []
        while count < search_engine_no:
            search_engines.append(lines.pop())
            count += 1
        query_no = int(lines.pop())
        count = 0
        queries = []
        while count < query_no:
            queries.append(lines.pop())
            count += 1
            
        yield search_engine_no, search_engines, queries

def count_switch(search_engine_no, search_engines, queries):
    switch = 0
    search_engines = set(search_engines)
    q = set()
    for query in queries:
        if query in search_engines:
            q.add(query)
            if len(q) == search_engine_no:
                q.clear()
                q.add(query)
                switch += 1
            
    return switch
        
        
if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    wfile = open(out_file, 'w')
    case_no = 1
    for search_engine_no, search_engine, queries in read_file(in_file):
        switch = count_switch(search_engine_no, search_engine, queries)
        wfile.write('Case #'+str(case_no)+': '+str(switch)+'\n')
        case_no += 1
    





#END