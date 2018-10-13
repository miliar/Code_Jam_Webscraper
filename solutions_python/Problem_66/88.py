#!/usr/bin/env python

def parse_testcase(itr):
    p=parse_countline(itr)
    ml=map(int,itr.next().strip().split())
    sl=[[]]*p
    for i in range(p):
        sl[i]=map(int,itr.next().strip().split())
    return p,ml,sl

def proc_testcase(tc):
    p,ml,sl=tc
    rtvl = []
    for i in range(p):
        rtvl.append([0 for j in range(1<<p)])
    for i in range(1<<p):
        for cnt in range(p-ml[i]):
            rtvl[p-cnt-1][i/(1<<(p-cnt))]=1
    r=0
    for i in range(p):
        for j in range(1<<(p-1-i)):
            if rtvl[i][j] ==1:
                r+=sl[i][j]
    return str(r)
                           
def parse_file(fstr):
    itr=iter(fstr)
    c=parse_countline(itr)
    for i in range(1,c+1):
        yield(i,parse_testcase(itr))

def parse_countline(itr):
    return int(itr.next().strip())

def parse_numbersline(itr):
    l=itr.next().strip().split()
    return tuple(map(int,l))

def main(argv):
    ifstr=open(argv[0],'rU')
    ofstr=open(argv[1],'wb')
    for i, tc in parse_file(ifstr):
        ofstr.write('Case #%d: %s\n'%(i, proc_testcase(tc)))
    ofstr.close()
    ifstr.close()

if __name__=='__main__':
    import sys
    main(sys.argv[1:])
    
