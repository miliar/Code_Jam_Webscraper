
import sys

def main():
    f = 'magician.sample'
    f = sys.argv[1]
    f = open(f)
    N = int(f.readline())
    for i in xrange(N):
        a,b = p(f), p(f)
        print 'Case #%d:'%(1+i), solve(a,b)

def p(f):
    n = int(f.readline())
    s = p2(f)
    return s[n-1]

def p2(f):
    o=[]
    for i in xrange(4):
        l = map(int, f.readline().strip().split())
        o.append(set(l))
    return o

def solve(a,b):    
    m = a.intersection(b)
    if len(m)==0:
        return 'Volunteer cheated!'
    elif len(m)==1:
        return m.pop()
    else:
        return 'Bad magician!'

    
main()
