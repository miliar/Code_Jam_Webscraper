import sys, math, collections

def main():
    inFile = open('A-large.in', 'rt')
    outFile = open(inFile.name.replace('.in', '.out'), 'wt')
#    outFile = sys.__stdout__
    Rope = collections.namedtuple('Rope', 'a b')
    T = int(inFile.readline())
    for t in xrange(1,T+1):
        N = int(inFile.readline().strip())
        ropes = []
        for j in xrange(N):
            x,y = map(int, inFile.readline().strip().split(' '))
            ropes.append(Rope(a=x,b=y))
        intersections = 0
        for j in xrange(N):
            p = ropes[j]
            for k in xrange(j+1,N):
                q = ropes[k]
                if (p.a<q.a and p.b>q.b) or (p.a>q.a and p.b<q.b):
                    intersections += 1
        outFile.write('Case #%d: %d\n' % (t, intersections))
    outFile.close()
        

if __name__ == '__main__':
    main()
