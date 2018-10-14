def FindFirst(s,  q):
    max = 0
    for x in s:
        if(x not in q):
            max = len(q)
            break
        if(q.index(x) > max):
            max = q.index(x)
    return max
filename = 'SavingTheUniverse-A-large'
input = open(filename + '.in',  'r')
output = open(filename + '.out',  'w')
Cases = int(input.readline().rstrip())
for i in xrange(1, Cases+1):
    S = int(input.readline().rstrip())
    Engines = []
    for j in xrange(S):
        Engines.append(input.readline().rstrip())
    Q = int(input.readline().rstrip())
    Queries = []
    for j in xrange(Q):
        Queries.append(input.readline().rstrip())
    next = 0
    if Q == 0:
        switch = 0
    else:
        switch = -1
    while next <= Q-1:
       next += FindFirst(Engines,  Queries[next:])
       switch += 1
    output.write('Case #' + str(i) + ': ' + str(switch) + '\n')
output.close()
