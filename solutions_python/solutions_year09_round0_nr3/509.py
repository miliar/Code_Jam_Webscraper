#!/usr/bin/env python

import sys,itertools

"""
tests=[('elcomew elcome to code jam','0001'),
       ('wweellccoommee to code qps jam','0256'),
       ('welcome to codejam','0000'),
       ('we sent you a welcoming email, to welcome you to code jam. but its possible that you still dont feel welcomed to code jam. thats why we decided to name a problem welcome to code jam. after solving this problem, we hope that youll feel very welcome. very welcome, that is, to code jam.','0')]
"""
#tests=[('1123231','0'),]

#tests=[('wweellccoommee to code qps jam','0256'),]

ss='welcome to code jam'
#ss='123'


def find_all(sstr,cchar):
    r=[]
    pos=sstr.find(cchar)
    while pos>-1:
        r.append(pos)
        pos=sstr.find(cchar,pos+1)
    return r


def find_char_pos(s):
    print s
    a=[]
    for i,c in enumerate(ss):
        aa=find_all(s,c)
        a.append(aa)
    return a


def is_growing(lst):
    last=-1
    for x in lst:
        if x<last: return False
        last=x
    return True

def trim(pa):
    for i in range(0,len(pa)-1):
        for x in pa[i]:
            if len(pa[i+1])>0:
                if x>pa[i+1][-1]:
                    #print 'del',pa[i][pa[i].index(x):],'from row',i
                    del pa[i][pa[i].index(x):]
                    break;
    for i in range(1,len(pa)):
        for x in pa[i]:
            if len(pa[i-1])>0:
                if x<pa[i-1][0]:
                    #print 'del',x,pa[i][:pa[i].index(x)+1],'from row',i
                    del pa[i][:pa[i].index(x)+1]
                    break;

def count_occ(pa):
    #for i in range(0,len(pa)):
    #    print ss[i],'>',pa[i]

    trim(pa)

    #for i in range(0,len(pa)):
    #    print ss[i],'>',pa[i]

    c=0
    for x in itertools.product(*pa):
        if is_growing(x):
            #print x,'OK',c
            c+=1

    res=('0000%d' % c)[-4:]
    return res

"""

123

0123456

1123231
x xx
x   xx
x x  x
 xxx
 x  xx
 xx  x



"""


lines=open(sys.argv[1],'r').read().split('\n')
test_count=int(lines[0])
tests=lines[1:]

out=open('output.txt','w')

for i,test in enumerate(tests):
    if i<test_count:
        t=test.lower()
        pa=find_char_pos(t)
        c=count_occ(pa)
        print 'Case #%d: %s' % (i+1,c)
        out.write('Case #%d: %s\n' % (i+1,c))

out.close()
