f = open('C-large.in','r')
o = open('C-large.out','w')

q = int(f.readline())

for i in xrange(q):
    o.write('Case #' + str(i+1) + ': ')
    
    N = int(f.readline())
    Q = f.readline().split()
    P = ([int(Q[j]) for j in xrange(N)])
    P.sort() 

    a = [0 for j in xrange(24)]
    for x in P:
        for y in xrange(24):
            if (x >> y):
                a[y] += (x >> y) % 2
            else : break
    
    possible = True

    for j in a:
        if j % 2:
            possible = False

    if possible: o.write('%i' % sum(P[1:]))
    else : o.write('NO')
        
    o.write('\n') 
