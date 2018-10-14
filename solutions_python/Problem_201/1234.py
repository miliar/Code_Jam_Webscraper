def read_case(line):
    l = line.split(' ')
    return (int(l[0]),int(l[1]))

def read_input(path):
    f = open(path, 'r')
    g = open(path+'_res.txt', 'w')
    T = int(f.readline())
    for i in xrange(T):
        line = f.readline()
        g.write('Case #%d: ' % (i+1))
        n,k = read_case(line)
        a,b = solve(n,k)
        g.write(str(a)+' '+str(b))
        g.write('\n')
    g.close()
    f.close()
    
def solve(n, k):
    if k == 1:
        return n/2,(n-1)/2
    if k%2 == 0:
        return solve(n/2,k/2)
    #k%2 == 1
    return solve((n-1)/2,k/2)

read_input('C-large.in')

#for simulation
def L_R(s,i):
    for L in xrange(i-1,-1,-1):
        if s[L]:
            break
    for R in xrange(i+1,len(s)):
        if s[R]:
            break
    l,r = (i-L-1,R-i-1)
    return max(l,r),min(l,r)

def choose_stall(s):
    Mmin,Mmax = -1,-1
    M = 0
    for i in xrange(len(s)):
        if not s[i]:
            x,n = L_R(s,i)
            if n > Mmin or (n == Mmin and x > Mmax):
                Mmin = n
                Mmax = x
                M = i
    return M,Mmax,Mmin
    
def sim(n,k):
    s = [1] + [0]*n + [1]
    for i in xrange(k-1):
        c = choose_stall(s)[0]
        s[c] = 1
    c,a,b = choose_stall(s)
    if (a,b) != solve(n,k):
        print 'failed'
        print n,k
        print a,b
        print solve(n,k)

def sim_sim(n): return sim(n,n)
        
