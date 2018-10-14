#!/usr/bin/env python

def parse_testcase(itr):
    nn,kk=parse_numbersline(itr)
    rl=[]
    for i in range(nn):
        l=itr.next().strip().strip('.')
        rl.append(l)
    return nn,kk,rl

def update_listR(l,o,kk):
    if l[o] >= 0:
        l[o] += 1
        if l[o] == kk:
            return 1
    else:
        l[o] = 1
    return 0

def update_listB(l,o,kk):
    if l[o] <= 0:
        l[o] -= 1
        if l[o] == -kk:
            return 2
    else:
        l[o] = -1
    return 0

def proc_testcase(tc):
    nn,kk,rl=tc
    dl=2*nn-1
    column=[0]*nn
    row=[0]*nn
    d1=[0]*dl
    d2=[0]*dl
    dub=2*nn-kk
    x=0
    winner=0
    for l in rl:
        y=0
        for c in reversed(l):
            if c == 'R':
                winner = winner | update_listR(column,x,kk)
                winner = winner | update_listR(row,y,kk)
                d1o = x+y+1
                if d1o>= kk and d1o <= dub:
                    winner = winner | update_listR(d1,d1o-1,kk)
                d2o = x-y+nn
                if d2o >=kk and d2o <= dub:
                    winner=winner | update_listR(d2,d2o-1,kk)
                y+=1
            if c == 'B':
                winner = winner | update_listB(column,x,kk)
                winner = winner | update_listB(row,y,kk)
                d1o = x+y+1
                if d1o>= kk and d1o <= dub:
                    winner = winner | update_listB(d1,d1o-1,kk)
                d2o = x-y+nn
                if d2o >=kk and d2o <= dub:
                    winner=winner | update_listB(d2,d2o-1,kk)
                y+=1
        x+=1
    if winner == 0:
        return 'Neither'
    elif winner == 1:
        return 'Red'
    elif winner == 2:
        return 'Blue'
    return 'Both'
        

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
    
