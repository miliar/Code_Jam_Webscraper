import string

fin = open ( 'B-large.in', 'r' )
fout = open ( 'B-large.out', 'w' )

C = int(fin.readline ( ))
for c in range(1,C+1):
    elem = fin.readline().split ( ' ' )
    n = int(elem[0])
    k = int(elem[1])
    b = int(elem[2])
    t = int(elem[3])
    
    elem = fin.readline().split(' ')
    x = [ int(val) for val in elem]
    elem = fin.readline().split ( ' ' )
    v = [ int(val) for val in elem]

    toskip = 0
    swap = 0
    tosearch = k
    r = range(n)
    r.reverse()
    for i in r:
        if x[i]+v[i]*t >= b:
            swap += toskip
            tosearch -= 1
        else:
            toskip += 1
        if tosearch == 0:
            break

    if tosearch == 0:
        fout.write ( 'Case #%d: %d\n' % ( c, swap) )
    else:
        fout.write ( 'Case #%d: IMPOSSIBLE\n' % c )

print 'done'
fout.close()