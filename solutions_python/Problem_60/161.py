#!/usr/bin/env python

class chick():
    def __init__(self, loc, speed):
        self.loc = loc
        self.speed = speed
        self.conf = 0

def comp(x, y):
    if x.conf < y.conf:
        return -1
    elif x.conf > y.conf:
        return 1
    else:
        return 0

def main():
    fin = open('large.in','r')
    fout = open('large.out','w')
    c = int(fin.readline())
    for test in range(c):
        loc = []
        speed = []
        reach = []
        unreach = []
        n,k,b,t = fin.readline().split(' ')
        n = int(n)
        k = int(k)
        b = int(b)
        t = int(t)
        #print 'k = ',k
        for item in fin.readline().split(' '):
            loc.append(int(item))
        for item in fin.readline().split(' '):
            speed.append(int(item))
        for i in range(n):
            if (1. * (b - loc[i]) / speed[i] <= t):
                reach.append(chick(loc[i],speed[i]))
            else:
                unreach.append(chick(loc[i],speed[i]))
        for reachitem in reach:
            for unreachitem in unreach:
                if (reachitem.speed > unreachitem.speed\
                        and reachitem.loc < unreachitem.loc):
                    #print 'debug'
                    if 1.0*(unreachitem.loc - reachitem.loc)/(reachitem.speed - unreachitem.speed)*reachitem.speed+reachitem.loc < b:
                        #print 'debug'
                        reachitem.conf += 1
        reach.sort(comp)
        #for item in reach:
        #    print item.loc, item.speed, item.conf
        #print '----------'
        #for item in unreach:
        #    print item.loc, item.speed, item.conf
        #print '============='
        count = 0
        if len(reach) < k:
            ans = 'IMPOSSIBLE'
        else:
            for i in range(k):
                count += reach[i].conf
            ans = str(count)
        fout.write('Case #%d: %s\n' % (test+1,ans))
    fin.close()
    fout.close()
if __name__ == '__main__':
    main()
