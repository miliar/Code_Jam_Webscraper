def find_engine(Q,E):
    dist_list = [0]*len(E)
    for e in E:
        for q in Q:
            if e == q: # if it is equal, dist_list is the minimun distance
                #dist_list[E.index(e)] += 1
                break 
            else: dist_list[E.index(e)] += 1
    
    max = dist_list[0]
    index = 0
    for t in range(1,len(dist_list)):  #find the longest distance
        if dist_list[t] > max:
            max = dist_list[t]
            index = t
    return index        
        
    

f = open("A-large.in","r")
fp=open("output.txt", 'w')
line = f.readline()
cases = int(line)
line = f.readline()
noc = 0
while line:
    n_engines = int(line)
    engines = []
    for j in range(0,n_engines):
        line = f.readline()
        engines.append(line)
    line = f.readline()
    n_queries = int(line)
    queries = []
    for j in range(0,n_queries):
        line = f.readline()
        queries.append(line)
    switch = 0
    y = find_engine(queries,engines)
    while queries:
        p = queries[0]   #first element of queries
        if engines[y] == p:  # there is a switch
            switch += 1 
            y = find_engine(queries,engines)
        queries.remove(p)
    noc += 1
    oup = "Case #"+str(noc)+": "+str(switch)+"\n"
    fp.write(oup)
    line = f.readline()

f.close()
fp.close()

    

