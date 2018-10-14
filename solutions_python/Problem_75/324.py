import sys

f = open('blarge.in','r')
#f = sys.stdin
t = int(f.readline().strip())

for z in xrange(t):
    ln = f.readline().strip().split()
    i,c = 1,int(ln[0])
    com = {}
    for ci in xrange(c):
        tp = ln[ci+i]
        com[(tp[0],tp[1])]=tp[2]
        com[(tp[1],tp[0])]=tp[2]
    #print com
        
    d = int(ln[1+c])
    dest = []
    for di in xrange(d):
        tp = ln[di+c+2]
        dest.append((tp[0],tp[1]))
        dest.append((tp[1],tp[0]))
        
    #n = ln[2+c+d]
    l,s = [],ln[-1]
    for si in s:
        bad=False
        for li in l:
            if (li,si) in dest and (si,l[-1]) not in com: bad=True
        if bad: l=[]
        else:
            l.append(si)
            while len(l)>1:
                last = (l[-2],l[-1])
                if last in com:
                    l.pop()
                    l.pop()
                    l.append(com[last])
                else : break
    out = 'Case #'+str(z+1)+': ['+', '.join(l)+']'
    print out
    #print l
                
    
