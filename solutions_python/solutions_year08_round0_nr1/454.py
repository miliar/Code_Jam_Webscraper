tcs = input()
output = []
for i in range(tcs):
    x = input()
    search_engines = []
    queries = []
    for i in range(x):
        search_engines.append(raw_input())
    y = input()
    for i in range(y):
        queries.append(raw_input())
    def anyUnique(se, qs):
        return len(set(se) - set(qs))
    def find_switch(search_engines, queries):
        if anyUnique(search_engines, queries):
            return 0
        else:
            id = 0
            for each in search_engines:
                if each in queries and queries.index(each) > id:
                    id = queries.index(each)
            return 1 + find_switch(search_engines, queries[id:])
    output.append(find_switch(search_engines,queries))

for i in range(tcs):
    print 'Case #%d: %d' % (i+1,output[i])
