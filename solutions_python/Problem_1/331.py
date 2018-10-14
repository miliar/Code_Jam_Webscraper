def google (engines, queries):
    switch = 0
    while 1:
        max = 0 
        for item in engines:
            try:
                indi = queries.index(item)
            except ValueError:
                return switch
            if indi > max:
                max = indi
        switch = switch + 1
        del queries[0: max]
        

f = open("abc.in")
w = open("output.ot", 'w')
N = int (f.readline().strip())
for i in range(N):
    S = int (f.readline().strip())
    engines = []
    queries = []
    for j in range(S):
        engine = f.readline().strip()
        engines.append(engine)
    Q = int (f.readline().strip())
    for j in range(Q):
        query = f.readline().strip()
        queries.append(query)
            
    result = "Case #%d: %d" % ((i +1), google (engines, queries)) + "\n"
    w.write(result)
f.close()
w.close()



