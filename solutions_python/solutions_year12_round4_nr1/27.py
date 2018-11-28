# A
from sys import stdin, stderr

def tryv():
    global N, v, D
    
    if v[0][1] < v[0][0]: return 'NO'
    
    st = [ 0 ]
    pst = 0
    
    while pst<len(st):
        i = st[pst]
        pst += 1
        if pst % 1000 == 0:
            print >>stderr, pst
        
        f = v[i][2]
        t = v[i][0]*2 - f
        if t>=D: return 'YES'
        
        
        for j in xrange(i+1, N):
            #print t, v[j], v[j][1]>=v[j][0]-v[i][0]
            w = max(v[i][0], v[j][0] - v[j][1])
            if v[j][0] > t: break
            if v[j][0]<= t and (v[j][2] == 0 or v[j][2] > w):
                v[j][2] = w
                st.append(j)
                #print i, j, v[j]
                
    return 'NO'
    

T=int(stdin.readline())
for t in xrange(1, T+1):
    N=int(stdin.readline())
    v = []
    for i in xrange(N):
        v.append(map(int, stdin.readline().split()) + [0])
    D=int(stdin.readline())
    
    print 'Case #%d: %s' % (t, tryv())
    