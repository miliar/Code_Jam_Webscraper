'''
Created on May 20, 2011

@author: ola
'''
import math
from operator import itemgetter

def cwp(games):
    c1 = games.count('1')
    c0 = games.count('0')
    tot = c0+c1
    wp = 1.0*c1/tot if tot != 0 else 0
    #print games,wp
    return wp

def cowp(data,index):
    #print "cowp",index
    nd = [list(x) for x in data]
    mine = nd[index]
    tot = 0.0

    for i,x in enumerate(mine):
        if x == '.': continue
        nd[i][index] = '.'
    c = 0
    for i,x in enumerate(nd):
        if i == index: continue
        if mine[i] == '.': continue
        tot += cwp(''.join(x))
        c += 1
    return tot/c if c != 0 else 0.0

def calc(data):
    wp = [0]*len(data)
    owp = [0]*len(data)
    oowp = [0]*len(data)
    for i,x in enumerate(data):
        wp[i] = cwp(x)
        owp[i] = cowp(data,i)
    for i,x in enumerate(data):
        d = []
        for j,ch in enumerate(x):
            if ch == '.': continue
            d.append(owp[j])
        if len(d) == 0:
            oowp[i] = 0.0
        else:
            oowp[i] = 1.0*sum(d)/len(d)
    for i in xrange(len(data)):
        rp = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]
        print rp
            

def one(n):
    teams = int(raw_input())
    data = []
    for x in xrange(teams):
        line = raw_input()
        data.append(line)
    print "Case #%d: " % (n)
    calc(data)
        

def main():
    n = int(raw_input())
    for x in xrange(n):
        one(x+1)

if __name__ == "__main__":
    main()