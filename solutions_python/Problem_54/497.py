from fractions import gcd
from itertools import izip

def gcd_list(X):
    if len(X) == 1: return X
    g = gcd(X[0],X[1])
    for x in X:
        if g == 1: return 1
        g = gcd(g,x)
    return g

def common_diff(g,X):
    if g == 1 : return 0
    return g - (X[0] % g if X[0]%g != 0 else g) 

def warn(T):
    if len(T) == 2: return common_diff(abs(T[0]-T[1]),T)
    diffs = [abs(x-y) for x,y in izip(T[1:],T[:-1])]
    return common_diff(gcd_list(diffs),T)

def print_res(caseno,res):
    print "Case #%d: %s" %(caseno,res) 

def main():
    for case in xrange(1,int(raw_input())+1):
        T = [long(w) for w in raw_input().split(' ')][1:]
        print_res(case,warn(T))

if __name__=="__main__":
    main()
