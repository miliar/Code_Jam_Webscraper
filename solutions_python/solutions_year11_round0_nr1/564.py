inf = open('A-large.in', 'r')
outf = open('A-large.out', 'w')

def incdec(n,nexn):
    if nexn > n:
        return n+1
    elif nexn < n:
        return n-1
    else:
        return n

T = int(inf.readline())
for ti in range(1, T+1):
    line = inf.readline().rstrip().split(' ')
    N = int(line[0])
    line.pop(0)
    R = line[::2]
    P = line[1::2]
    
    t = 0
    o = 1
    nexo = 1
    b = 1
    nexb = 1
    while len(P)!=0:
        if 'O' in R:
            nexo = int(P[R.index('O')])
        else:
            nexo = o
            
        if 'B' in R:
            nexb = int(P[R.index('B')])
        else:
            nexb = b

        if R[0] == 'O':
            while (nexo != o):
                o = incdec(o,nexo)
                b = incdec(b,nexb)
                t+=1
            t+=1
            b=incdec(b,nexb)
        else:
            while b != nexb:
                o = incdec(o,nexo)
                b = incdec(b,nexb)
                t+=1
            t+=1
            o=incdec(o,nexo)
        P.pop(0)
        R.pop(0)
    
    print "Case #" + str(ti) + ": " + str(t)
    outf.write("Case #" + str(ti) + ": " + str(t) + "\n")

inf.close()
outf.close()
