import time

##import sys
##sys.setrecursionlimit(10002)
INFILE = 'bl.in'
OUTFILE = 'b.out'


def solve(c,d,cx,dx):
    if c+d<=1:
        return 2
    mx=[[i[0],i[1],0] for i in cx]+[[i[0],i[1],1] for i in dx]
    mx.sort()
    ans=0
    ctime=0
    dtime=0
    free=[[],[]]
    i=0
    while i<c+d:
        stime=mx[i][0]
        while i+1<c+d and mx[i][2]==mx[i+1][2]:
            free[mx[i][2]].append(mx[i+1][0]-mx[i][1])
            i += 1
        etime=mx[i][1]
        if mx[i][2]==0:
            ctime+=etime-stime
        else:
            dtime+=etime-stime
        if i+1<c+d:
            ans+=1
            i+=1
        else:
            break
    # print ctime,dtime,ans,free
    if mx[0][2]<>mx[-1][2]:
        ans+=1
    elif mx[0][2]==0:
        free[0].append(mx[0][0]+1440-mx[-1][1])
        ctime+=free[0][-1]
    else:
        free[1].append(mx[0][0]+1440-mx[-1][1])
        dtime+=free[1][-1]
    # print ctime,dtime,ans,free
    if ctime<=720 and dtime<=720:
        return ans
    if ctime>720:
        dt=ctime-720
        lt=free[0]
        lt.sort(reverse=1)
        i=0
        while dt>0:
            dt-=lt[i]
            i+=1
            ans+=2
    else:
        dt = dtime - 720
        lt = free[1]
        lt.sort(reverse=1)
        i = 0
        while dt > 0:
            dt -= lt[i]
            i += 1
            ans += 2
    return ans


def read_input(fi):
    read = lambda type: type(fi.readline()[:-1])
    readArray = lambda type: map(type, fi.readline().split())
    readMatrix = lambda type, x: [map(type, fi.readline().split()) for i in range(x)]
    readLines = lambda type, x: [type(fi.readline()[:-1]) for i in range(x)]
    c,d = readArray(int)
    cx=readMatrix(int,c)
    dx=readMatrix(int,d)
    return c,d,cx,dx


def main():
    fi = file(INFILE)
    fo = file(OUTFILE, 'w')
    time0 = time.time()
    t = int(fi.readline())
    for ti in range(t):
        time1 = time.time()
        ans = "Case #%d: %s" % (ti + 1, solve(*read_input(fi)))
        print ans, "%.3f" % (time.time() - time1)
        fo.write(ans + '\n')
    print "%.3f" % (time.time() - time0)
    fi.close()
    fo.close()


if __name__ == '__main__':
    main()
    import random
    # s=list('RBY'*333)
    # random.shuffle(s)
    # time0=time.time()
    # print solve(999,333,0,333,0,333,0),time.time()-time0
