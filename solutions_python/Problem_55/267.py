import sys

def ride(k,l):
    c=0
    on=[]
    while len(l)>0 and c+l[0]<=k:
        g=l.pop(0)
        on.append(g)
        c+=g
    l.extend(on)
    return c

def day(r,k,l):
    tot=0
    for i in xrange(r):
        tot+=ride(k,l)
    return tot

def main():
    c=int(sys.stdin.readline().rstrip('\n'))
    for i in xrange(c):
        R,K=map(lambda l: int(l), sys.stdin.readline().split()[:2])
        L=map(lambda l: int(l), sys.stdin.readline().split())
        print "Case #%d: %s"%((i+1),day(R,K,L))


if __name__ == "__main__":
    main()


