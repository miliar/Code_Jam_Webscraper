'''
Infinite House of Pancakes
'''
import sys
import math

negcmp = lambda x, y: -cmp(x, y)
def case(D, P):
    P.sort(negcmp)
    min_minutes = P[0]
    target_start = int(math.floor(P[0]**0.5))
    for target in range(target_start, P[0]):
        minutes = 0
        p = P[:]
        while p[0] > target:
            d = int(math.ceil(p[0] / float(target)))
            if d == 1:
                break
            minutes += d - 1
            div = p[0] / d
            mod = p[0] % d
            A = ([div + 1] * mod) + ([div] * (d - mod))
            del p[0]
            p += A
            p.sort(negcmp)
        minutes += p[0]
        if minutes < min_minutes:
            min_minutes = minutes
    return str(min_minutes)

def readargs(f):
    D = int(f.readline().strip())
    P = list(map(int, f.readline().strip().split(' ')))
    return (D, P)

def gcjmain():
    if len(sys.argv) == 1 or sys.argv[1] == "-":
        f = sys.stdin
    else:
        f = open(sys.argv[1])
    
    T = int(f.readline())
    for i in range(T):
        args = None
        while args == None:
            args = readargs(f)
        output = case(*args)
        print 'Case #%d: %s' % (i+1, output)
    
    f.close()

if __name__ == '__main__':
    gcjmain()