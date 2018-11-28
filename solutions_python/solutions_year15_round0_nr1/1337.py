'''
Standing Ovation
'''
import sys

def case(Smax, Svalues):
    added = 0
    for i in range (1, Smax + 1):
        n = sum(Svalues[:i])
        if n < i:
            tmp = i - n
            added += tmp
            Svalues[0] += tmp
        
    return str(added)

def readargs(f):
    line = f.readline().strip().split(' ')
    Smax = int(line[0])
    Svalues = map(int, line[1])
    return (Smax, Svalues)

def gcjmain():
    if len(sys.argv) == 1 or sys.argv[1] == "-":
        f = sys.stdin
    else:
        f = open(sys.argv[1])
    
    N = int(f.readline())
    for i in range(N):
        args = None
        while args == None:
            args = readargs(f)
        output = case(*args)
        print 'Case #%d: %s' % (i+1, output)
    
    f.close()

if __name__ == '__main__':
    gcjmain()