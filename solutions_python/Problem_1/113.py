#!/usr/bin/python
def minimum(a,b):
    if a<b:
        return a
    return b

n=input()
inf = 10000000
for z in range(n):
    m=input()
    eng = []
    for i in range(m):
        eng.append(raw_input())
    q=input()
    if q==0:
        print "Case #" + str(z+1) + ": 0"
        continue

    query = []
    for i in range(q):
        query.append(raw_input())
    # # #

    mat=[]
    mini=[]
    for i in range(q):
        mat.append([])
        for l in range(m):
            mat[i].append([])
        mini.append(inf)
    
    # # #
    ind = eng.index(query[0])
    mat[0][ind] = inf
    for i in range(m):
        if i != ind:
            mat[0][i] = 0
    mini[0] = 0

    for w in range(1,q):
        ind = eng.index(query[w])
        mat[w][ind] = inf

        for i in range(m):
            if i != ind:
                mat[w][i] = minimum(mini[w-1]+1,mat[w-1][i])

            mini[w] = minimum(mini[w], mat[w][i])
    #print mat
    print "Case #" + str(z+1) + ": " + str(mini[q-1])
