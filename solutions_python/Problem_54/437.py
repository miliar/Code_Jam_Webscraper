import sys
import decimal as d

def main():
    inFile = open(sys.argv[1], 'rt')
    outFile = open(inFile.name.replace('.in', '.out'), 'wt')
#    outFile = sys.__stdout__
    C = int(inFile.readline())
    for t in xrange(1,C+1):
        vals = map(d.Decimal, inFile.readline().strip().split(' '))
        res = processCase(vals[1:])
        outFile.write('Case #%d: %d\n' % (t, res))
    outFile.close()
        
def processCase(t):
    t.sort()
    recent = t[0]
    diffs = map(lambda x: x - recent, t)[1:]
    gcd = findListGCD(diffs)
    e = (recent / gcd).to_integral_value(rounding = d.ROUND_UP)
    return gcd*e - recent
    
def findListGCD(l):
    if len(l)==1:
        return l[0]
    res = findGCD(l[0], l[1])
    if len(l)==2:
        return res
    return min(res, findListGCD([res].extend(l[2:])))
        

d0 = d.Decimal(0)
d1 = d.Decimal(1)
d2 = d.Decimal(2)

def findGCD(X,Y):
    if X==d0: return Y
    if Y==d0: return X
    if X==Y: return X
    if X==d1 or Y==d1: return d1
    ex = (X.as_tuple().digits[-1] % 2)==0
    ey = (Y.as_tuple().digits[-1] % 2)==0
    if ex and ey: return d2*findGCD(X/d2, Y/d2)
    if ex and not ey: return findGCD(X/d2, Y)
    if not ex and ey: return findGCD(X, Y/d2)
    return findGCD(Y, abs(X-Y))
#    if Y==
    
if __name__ == '__main__':
    main()
