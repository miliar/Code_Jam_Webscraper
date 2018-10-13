def s1(n,p):
    nn = 2**n

    if p>=nn:
        return nn-1

    cc = 1
    need = 0
    while p > nn/2:
        need += cc
        cc *= 2
        p -= nn/2
        nn /= 2
    need += cc
    return need-1
        
def s2(n,p):
    nn = 2**n

    if p>=nn:
        return nn-1

    cc = 1
    need = 0
    while p < nn/2:
        #print "::",p,nn
        need += cc
        cc *= 2
        nn /= 2
    need += cc
    #print "::",need
    return 2**n-1 - need
        
def solve(t):
    n,p = [int(x) for x in raw_input().split()]

    #print ">> ",2**n,p

    need1 = s1(n,p)
    need2 = s2(n,p)

    print "Case #%d: %d %d" %(t+1,need1,need2)

def main():
    t = int(raw_input())
    for i in range(t):
        solve(i)

main()
