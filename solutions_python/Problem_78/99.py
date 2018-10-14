import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def check(N, PD, PG):
    if PG == 0 and PD > 0:
        return False
    if PG == 100 and PD < 100:
        return False
    
    if PD == 0:
        return True
    d = 100 / gcd(100, PD)
    D = (N / d) * d
    #print "[", N, PD, PG, "]", d, D
    return D > 0


def main():
    f = open(sys.argv[1])
    if len(sys.argv) > 2:
        out = open(sys.argv[2], 'w')
    else:
        out = sys.stdout

    T = int(f.readline())   
    for t in range(1, T+1):
        N, PD, PG = [int(x) for x in f.readline().split()]
        if check(N, PD, PG):
            print >>out, "Case #%d: Possible" % t
        else:
            print >>out, "Case #%d: Broken" % t

if __name__ == "__main__":
    main()