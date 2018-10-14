f = open('B-large.in','r')
o = open('B-large.out','w')

q = int(f.readline())

for i in xrange(q):
    o.write('Case #' + str(i+1) + ': ')
	
    P = f.readline().split()
	
    C = int(P[0])
    D = int(P[C+1])
    N = int(P[C+D+2])

    res = ''
    for j in xrange(N):
        res += P[3+C+D][j]
        iv = False
        for x in xrange(C):
            c = P[1+x]
            if res[-2:] == c[0:2] or res[-1:-3:-1] == c[0:2]:
                res = res[:-2] + c[2]
                iv = True
                break
                
        if not iv:
            for x in xrange(D):
                p = P[2+C+x]
                if res[-1] in p:
                    k = p.replace(res[-1],'') 
                    if k in res:
                        res = ''
                        break
                    
    
    o.write('[')
    for j in xrange(len(res)):
        if j: 
            o.write(', ')
        o.write(res[j])
    o.write(']')
    
    
    o.write('\n') 
