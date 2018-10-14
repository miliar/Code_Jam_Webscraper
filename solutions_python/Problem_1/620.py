fi = open("input.txt","r")
f = open("output.txt","w")

N = eval(fi.readline())

for n in range(N) :
    S = eval(fi.readline())
    engine = []
    for s in range(S) :
        a = fi.readline().strip()
        engine.append(a)
    Q = eval(fi.readline())
    query = []
    for q in range(Q) :
        a = fi.readline().strip()
        query.append(a)

    dy = []

    for q in range(Q) :
        min = 100000000
        for s in range(S) :
            for q2 in range(q+1) :
                if q2 == 0 :
                    if query[q2:q+1].count( engine[s] ) == 0 :
                        min = 0
                elif query[q2:q+1].count(engine[s]) == 0 and dy[q2-1]+1 < min :
                    min = dy[q2-1]+1
        dy.append(min)

    if Q == 0 :
        f.write("Case #" + str(n+1) + ": " + str(0) + "\n")
    else :
        f.write("Case #" + str(n+1) + ": " + str(dy[Q-1]) + "\n")

fi.close()
f.close()
