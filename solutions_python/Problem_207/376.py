import time

##import sys
##sys.setrecursionlimit(10002)
INFILE = 'bs.in'
OUTFILE = 'b.out'


def solve(n,r,o,y,g,b,v):
    d={}
    d['R']=r
    d['O']=o
    d['Y']=y
    d['G']=g
    d['B']=b
    d['V']=v
    l=['R','O','Y','G','B','V']
    l.sort(key=lambda x:(-d[x],x))
    ns={ }
    ns['R']={'B','Y','G'}
    ns['O']={'B'}
    ns['Y']={'R','B','V'}
    ns['G']={'R'}
    ns['B']={'R','Y','O'}
    ns['V']={'Y'}
    # print l,d
    ans=['']*n
    avas={'R','O','Y','G','B','V'}
    for i in range(n):
        for j in l:
            if j in avas and d[j]>0:
                ans[i]=j
                d[j]-=1
                avas=ns[j]
                l.sort(key=lambda x: (-d[x], x<>ans[0],x))
                break
        else:
            return 'IMPOSSIBLE'
    if ans[0]==ans[-1]:
        return 'IMPOSSIBLE'
    return ''.join(ans)


def read_input(fi):
    read = lambda type: type(fi.readline()[:-1])
    readArray = lambda type: map(type, fi.readline().split())
    readMatrix = lambda type, x: [map(type, fi.readline().split()) for i in range(x)]
    readLines = lambda type, x: [type(fi.readline()[:-1]) for i in range(x)]
    n,r,o,y,g,b,v = readArray(int)
    return n,r,o,y,g,b,v


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
