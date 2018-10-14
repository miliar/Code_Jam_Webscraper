import math,sys

def probmk (m, k, pmatrix):
    if pmatrix[m-2][k] != 0:
        return pmatrix[m-2][k]
    else:
        if m == k:
            pmatrix[m-2][k] = 1
            return 1
        elif k == m-1:
            pmatrix[m-2][k] = 0
            return 0
        elif m == 2 and k == 0:
            pmatrix[m-2][k] = 1
            return 1
        elif k != 0:
            pmatrix[m-2][k] = math.factorial(m)/(math.factorial(m-k)*math.factorial(k))*pmatrix[m-2-k][0]
            return pmatrix[m-2][k]
        elif k == 0:
            pmatrix[m-2][k] = math.factorial(m)
            for i in range(1,m+1):
                pmatrix[m-2][k] -= pmatrix[m-2][i]
            return pmatrix[m-2][k]
        else:
            print 'Prob error!'
            sys.exit(-1)

def estm (m, elist, pmatrix):
    print m
    if elist[m-2] != 0:
        return elist[m-2]
    else:
        elist[m-2] = 1.0
        print ' %f' % elist[m-2]
        for i in range(2, m):
            elist[m-2] += float(pmatrix[m-2][m-i])/float(math.factorial(m))*elist[i-2]
            print ' %f' % elist[m-2]
        elist[m-2] =  elist[m-2]/(1-float(pmatrix[m-2][0])/float(math.factorial(m)))
        print '  %f' % elist[m-2] 
        return elist[m-2]

if __name__ == '__main__':
    input = open('./source/D-large-0.in', 'r')
    output = open('./source/D-large-0.out', 'w')

    #n_max = 10
    #pmatrix = []
    #elist = []
    #for i in range(2,n_max+1):
    #    p =[]
    #    for j in range(i+1):
    #        p.append(0)
    #    pmatrix.append(p)
    #    elist.append(0)
            
    #for i in range(2, n_max+1):
    #    for j in reversed(range(i+1)):
    #        probmk(i,j,pmatrix)
    #for i in range(2, n_max+1):
    #    estm(i, elist, pmatrix)

    total = int(input.readline().strip())
    for i in range(total):
        est = 0
        N = int(input.readline().strip())
        seq = input.readline().strip().split()
        arr = [int(x) for x in seq]
        for j in range(N):
            if arr[j] != (j+1):
                est += 1.0    
        print >>output, "Case #%d: %.6f" % (i+1, est)
        
