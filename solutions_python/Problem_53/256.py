import sys
import numpy as np

def is_on(n,k):
    return k%pow(2,n)==(pow(2,n)-1)

def main():
    T=int(sys.stdin.readline().rstrip('\n'))
    for i,line in enumerate(sys.stdin):
        N,K=map(lambda l: int(l), line.split())
        print "Case #%d: %s"%((i+1),"ON" if is_on(N,K) else "OFF")

if __name__ == "__main__":
    main()
