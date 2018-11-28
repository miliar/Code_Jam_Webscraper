from decimal import *
import sys
import fractions

def find_y(l):
    getcontext().prec=10000
    l.sort()
    differences=map(lambda l: l[1]-l[0], zip(l[0:-1],l[1:]))
    gcd=reduce(lambda l,r: fractions.gcd(l,r), differences, 0)
    return str((Decimal(l[-1])/Decimal(gcd)).quantize(Decimal('1.'),rounding=ROUND_UP)*gcd-l[-1])

def main():
    c=int(sys.stdin.readline().rstrip('\n'))
    for i,line in enumerate(sys.stdin):
        l=map(lambda l: int(l), line.split()[1:])
        print "Case #%d: %s"%((i+1),find_y(l))

if __name__ == "__main__":
    main()
