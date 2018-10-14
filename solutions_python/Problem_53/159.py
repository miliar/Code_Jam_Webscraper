from numpy import *

FILE = open("A-large.in","r");

def Solve(N, K):
    if (K/(2**N) == (K+1)/(2**N)):
        return "OFF";
    else:
        return "ON";


T = int(FILE.readline());
for k in range(T):          # Each of the N cases:
    print "Case #%d:" %(k+1),
    [N,K] = map( int, FILE.readline().split() );
    print Solve(N,K);
