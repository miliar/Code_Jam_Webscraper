from sys import stdin

def main():
    n,k = map(int, stdin.readline().split())
    if (k+1)%(1<<n) == 0:
        return "ON"
    else:
        return "OFF"

tno = int(stdin.readline())
for i in xrange(0, tno):
    print "Case #%d: %s"%(i+1, main())
