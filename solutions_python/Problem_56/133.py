from fractions import gcd
from itertools import izip

def gravity(t):
    nt = []
    for l in t:
        spaces = l.count('.')
        r_str = '.'*spaces + l.replace('.','')
        nt.append(r_str)
    return nt
    
def rotate(t):
    return zip(*t[::-1])
    
def half(t):
    K = len(t[0])
    nt = []
    for i in range(K):
        nl = ''
        for x in range(i+1):
            nl += t[i-x][x]
        nt.append(nl)
    for i in range(K):
        nl = ''
        for y in range(i+1,K):
            nl += t[y][i-y]
        if nl:
            nt.append(nl)
    return nt
    
def chk_table(t,K):
    B_CHK = 'B'*K
    R_CHK = 'R'*K
    bflag = False
    rflag = False
    for l in t:
        l = ''.join(l)
        if l.find(B_CHK) != -1:
            bflag = True
        if l.find(R_CHK) != -1:
            rflag = True
    return (bflag,rflag)

def winner(table,K):
    bflag = False
    rflag = False
    g = gravity(table)
    tmpb,tmpr = chk_table(g,K)
    bflag = bflag or tmpb
    rflag = rflag or tmpr
    h = half(g)
    tmpb,tmpr = chk_table(h,K)
    bflag = bflag or tmpb
    rflag = rflag or tmpr
    r = rotate(g)
    tmpb,tmpr = chk_table(r,K)
    bflag = bflag or tmpb
    rflag = rflag or tmpr
    h = half(r)
    tmpb,tmpr = chk_table(h,K)
    bflag = bflag or tmpb
    rflag = rflag or tmpr
    return (bflag,rflag)

def print_res(caseno,res):
    rstr = 'Neither'
    if all(res):
        rstr = 'Both'
    elif res[0]:
        rstr = 'Blue'
    elif res[1]:
        rstr = 'Red'
    print "Case #%d: %s" %(caseno,rstr) 

def main():
    for case in xrange(1,int(raw_input())+1):
        N,K = [long(w) for w in raw_input().split(' ')]
        table = []
        for i in range(N):
            row = raw_input()
            table.append(row)
        print_res(case,winner(table,K))

if __name__=="__main__":
    main()
