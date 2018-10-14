'''
Created on May 7, 2010

@author: john
'''
from collections import deque

fname=r"c:\Users\john\Downloads\C-large"
fin = open(fname+".in")
fout = open(fname+".out","w")
T=int(fin.readline())

#pull groups from the queue
def pull(q,K):
    sum = 0
    tmp = []
    while len(q)>0 and sum+q[0]<=K:
        tmp.append(q.popleft())
        sum+=tmp[-1]
    q.extend(tmp)
    return sum

for t in xrange(T):
    R,K,N = map(int, fin.readline().split(" "))
    q = deque(map(int, fin.readline().split(" ")))
    
    #running EURO ;) sum 
    rsum = [0]
    dt = {}
    
    for r in xrange(R):
        tpl = tuple(q)
        if tpl in dt:
            dtp = dt[tpl]
            deltaIndex = r - dtp
            deltaSum = rsum[r]-rsum[dtp]
            rest = rsum[(R-r)%deltaIndex+dtp]-rsum[dtp]
            rsum.append(rsum[-1]+(R-r)/deltaIndex*deltaSum+rest)
            break
        else:
            dt[tpl]=r
            rsum.append(rsum[r]+pull(q,K))
    
    fout.write("Case #%d: %d\n" % (t+1,rsum[-1]))