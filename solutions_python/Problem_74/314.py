import sys

def go(c,l):
    st,p = [],1
    ls = [x[1] for x in l if x[0]==c]
    for li in ls:
        for _ in xrange(abs(p-li)):
            st.append(0)
        p=li
        st.append(1)
    return st

f = open('alarge.in','r')
#f = sys.stdin
t = int(f.readline().strip())

for z in xrange(t):
    ln = f.readline().strip().split()
    n = int(ln[0])
    l = []
    for j in xrange(n):
        l.append((ln[2*j+1], int(ln[2*j+2])))
        
    pos={'O':1,'B':1}
    t = 0
    steps= [go('O',l),go('B',l)]
    for li in l:
        prim = 0
        if li[0]=='B': prim=1
        fp=steps[prim].index(1)+1
        #print fp,
        t += fp
        steps[prim] = steps[prim][fp:]
        if steps[1-prim]:
            for _ in xrange(fp):
                if steps[1-prim][0]==0: steps[1-prim].remove(0)
        #print steps
    #print t
    print 'Case #'+str(z+1)+': '+str(t)
        
        
        
        
    
