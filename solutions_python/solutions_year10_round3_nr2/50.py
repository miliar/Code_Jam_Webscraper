from fractions import gcd
from itertools import izip

def acceptable(l,p,c):
    #print "T",l,p,c
    if (p/c) < l: return True
    if (p/c) == l and (p%c) == 0: return True
    return False
    
def div(l,c):
    if l % c != 0: return (l/c)+1
    return l / c

def test_count(L,P,C):
    #if acceptable(L,P,C): return 0
    tpoints = []
    p = P
    while not acceptable(L,p,C):
        p = div(p,C)
        #print "P",p 
        tpoints.append(p)
    tcount = len(tpoints)
    #print 'T',tpoints
    ret = 0
    while tcount:
        ret += 1
        tcount /= 2
    return ret

def print_res(caseno,res):
    print "Case #%d: %s" %(caseno,res) 

def main():
    for case in xrange(1,int(raw_input())+1):
        L,P,C = [long(w) for w in raw_input().split(' ')]
        print_res(case,test_count(L,P,C))

if __name__=="__main__":
    main()
