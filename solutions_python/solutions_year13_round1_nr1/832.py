import sys

def count(r,t):
    i=0
    s=0
    while True:
        s=s+2*r + 1 + (4*i)
        if s > t:
            return i
        i=i+1
        
        

n=int(sys.stdin.readline())
for i in range(0,n+1):
    r,t = [int(b) for b in sys.stdin.readline().split()]
    c=count(r,t)
    print"Case #"+str(i+1)+": "+str(c)
