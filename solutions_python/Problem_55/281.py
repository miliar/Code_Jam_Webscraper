from collections import deque

def sim(r,k,n):
    tot = 0
    rd = deque([])
    for i in range(0,r):
        sum = k
        rd = deque([])
        while sum-n[0]>=0:
            a = n.popleft()
            tot = tot+a
            sum = sum-a
            rd.append(a)
            if len(n)==0:
                break
        n.extend(rd) 
    return tot

f = file('C-small-attempt0.in','r')
count = 0
d1 = []
for l in f:
    if count!=0:
        if count%2==1:
            d1=[int(k) for k in l.split(" ")]
        else:
            d2=deque([int(k) for k in l.split(" ")])
            print "Case #%d: %d" % (count/2,sim(d1[0],d1[1],d2),)
            d1=[]
    count = count + 1
f.close() 
