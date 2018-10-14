from itertools import count
import psyco
def solve(d):
    for i in count():
        if not d: return i 
        e=set(d)
        #for i in range(6):
        #    print [1 if (j,i) in e else 0 for j in range(6)]
        #print
        for x,y in e:
            if (x-1,y) not in e and (x,y-1) not in e:
                 d.remove((x,y))
            if (x-1,y+1) in e:
                d.add((x,y+1))
                

psyco.full()
C=input()
for c in range(C):
    d=set()
    R=input()
    for i in range(R):
        x1,y1,x2,y2=map(int,raw_input().split())  
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                d.add((x,y))  
    print "Case #%s: %s"%(c+1,solve(d))

