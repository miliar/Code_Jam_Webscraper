import sys
import math

def main():
    #infile = open('in')
    #infile = open('A-large.in')
    infile = open('A-small-attempt0.in')
    #infile = open('A-small-practice.in')
    #infile = open('A-large-practice.in')
    outfile = open('out', 'w')
    T = long(infile.readline())
    for i in xrange(T):
        outfile.write('Case #'+str(i+1)+': ' + solve(infile) + '\n')

def getSmall(s):
    lc = '0'
    res = ''
    d = []
    for c in s:
        if c != lc:
            lc = c
            res += c
            d.append([c, 1])
        else:
            d[-1][1] = d[-1][1] + 1
    return (res, d)
    

def solve(infile):
    n = int(infile.readline())
    s = infile.readline().rstrip('\n')
    base, d = getSmall(s)
    ss = [d]
    ok = True
    for i in range(1, n):
        s = infile.readline().rstrip('\n')
        base2, d2 = getSmall(s)
        if base != base2:
            ok = False
            break
        else:
            ss.append(d2)
        
        
    if ok:
        res = 0
        for i in range(len(base)):
            med = int(round((sum(map(lambda x: x[i][1], ss)))/n))
            k = sum(map(lambda x: abs(x[i][1]-med), ss))
            res += k
        return str(res)
    else:
        return 'Fegla Won'

if __name__=='__main__':
    main()
