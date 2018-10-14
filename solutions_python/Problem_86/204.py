#!/usr/bin python
import sys
import fractions as f

def readline():
    return input.readline().strip(' \r\n\t')

input = sys.stdin

def lcm(a, b):
    return a * b // f.gcd(a, b)

def lcmm(*args):  
    return reduce(lcm, args)

def gcdd(*args):
    return reduce(f.gcd, args)

def check(musi,fr):
    for m in musi:
        if not (m%fr and fr%m):
            continue
        return False
    return True

T = int(readline())
for case in range(T):
    print "Case #"+str(case+1)+":",

    tmp = readline().split()
    N = int(tmp[0])
    L = int(tmp[1])
    H = int(tmp[2])
    
    musi = readline().split()
    musi = [int(x) for x in musi]

    #print musi
    #print "gcd", gcdd(*musi)
    #print "lcm", lcmm(*musi)
    for fr in range(L,H+2):
        if check(musi,fr):
            break
    
    if fr > H:
        print "NO"
    else:
        print fr



