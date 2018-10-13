in_file = "A-large.in"
out_file = "A-large.out"


def solve(engines, queries):
    c = -1
    while queries:
        for engine in engines:
            if not queries.count(engine):
                return str(c+1)

        q_len = len(queries)
        l = range(q_len)
        l.reverse()
        ind = 0
        for i in l:
            query = queries[i]
            if queries.count(query) == 1:
                if i > ind:
                    ind = i
                    break
            else:
                if (queries.index(query) > ind):
                    ind = queries.index(query)

        queries = queries[ind:q_len]
        c += 1

fr = open(in_file, 'r')
fw = open(out_file, 'w')
num_cases = int(fr.readline().strip())
for i in xrange(num_cases):
    s = int((fr.readline().strip()))
    search_engines = []
    for j in xrange(s):
        search_engines.append(fr.readline().strip())

    q = int((fr.readline()))
    queries = []
    for j in xrange(q):
        queries.append(fr.readline().strip())    

    #print i, search_engines, queries
    r = 0
    if q != 0:
        r = solve(search_engines, queries)
    #print r, "\n\n"
    fw.write("Case #" + str(i+1) + ": " + str(r) + "\n")

fr.close()
fw.close()
