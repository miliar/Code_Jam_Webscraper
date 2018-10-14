


f = open(r'C:\Ggl\qual\A-large.in')

numcases=int(f.readline())
for case in range(numcases):
    line=f.readline().strip()
    numengines=int(line)
    
    engines=[]
    for eng in range(numengines):
        line=f.readline().strip()
        engines.append(line)

    line=f.readline().strip()
    numqueries=int(line)

    queries=[]
    for que in range(numqueries):
        line=f.readline().strip()
        queries.append(line)

    forbiddenengines=[]
    switches=0
    for query in queries:
        if query not in forbiddenengines:
            forbiddenengines.append(query)
        if len(forbiddenengines) == len(engines):
            forbiddenengines=[query]
            switches += 1

    print "Case #" + str(case+1) + ": " + str(switches)


        






