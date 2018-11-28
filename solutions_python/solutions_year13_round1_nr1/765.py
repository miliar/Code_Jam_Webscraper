import sys
sys.stdin = open('A-small-attempt0.in', 'r')
sys.stdout = open('A-small-attempt0.out', 'w')
out = sys.stdout
N = input()
for i in range(1, N+1):
    out.write('Case #')
    out.write(str(i))
    out.write(': ')

    (r, t) = raw_input().split(' ')
    r = int(r)
    t = int(t)

    cost = 0
    n = 0
    while cost < t:
        cost += (r+1)**2-(r)**2
        #print cost
        r+=2
        if cost <= t:
            n += 1
    print n

    
##            n = 1.0000000000
##            
##            for i in range(0, 1000):
##                fx = n*r**2+2*n**2*r+2*n*r+2.0*(2*n**3+3*n**2+n)/3
##                fdx = r**2+4*n*r+2*r+2.0*(6*n**2+6*n+1)/3
##                print fx
##                n = n - fx/fdx
##
##            print n


sys.stdin.close()
sys.stdout.close()
