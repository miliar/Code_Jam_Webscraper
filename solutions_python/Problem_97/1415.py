__author__ = 'Raullen'
import collections
from sets import Set

f = open('C-small-practice.in','r')
T = int(f.readline())
g = open('res.out','w')
res = list()

def splitint(x):
    ret = list()
    for ch in str(x):
        ret.append(ch)
    return ret

def joindigits(digits):
    ret = ''
    for s in digits:
        ret += str(s)
    return int(ret)


for case in range(T):
    tmpAB = f.readline().split()
    A = int(tmpAB[0])
    B = int(tmpAB[1])

    cnt = Set()
    for i in range(A,B+1):
        mylist = collections.deque(splitint(i))
        for rot in range(1,len(mylist)):
            mylist.rotate(1)
            tmp = joindigits(mylist)
            if A <= tmp and tmp <= B:
                d = Set(); d.add(i); d.add(tmp)
                if len(d) == 2:
                    cnt.add(d)

    print 'Case #'+str(case+1)+': '+str(len(cnt))

g.writelines(res)
g.close()
f.close()
