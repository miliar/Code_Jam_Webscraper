from sys import stdin

def nwd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def main():
    a = map(int, stdin.readline().split())
    n = 0
    for x in a[2:]:
        n = nwd(n, abs(x-a[1]))
    return (n - a[1])%n

tno = int(stdin.readline())
for i in xrange(0, tno):
    print "Case #%d: %s"%(i+1, main())
