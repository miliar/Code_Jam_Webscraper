import sys, math, re

def main():
#    inFile = sys.__stdin__
#    outFile = sys.__stdout__
    inFile = open('D-large.in', 'rt')
    outFile = open(inFile.name.replace('.in', '.out'), 'wt')
    T = int(inFile.readline())
    for t in xrange(1,T+1):
        N = int(inFile.readline())
        a = map(int,inFile.readline().strip().split(' '))
        good = []
        bad = []
        for i in xrange(N):
            if a[i]==i+1:
                good.append(i)
            else:
                bad.append(i)
        outFile.write('Case #%d: %d\n' % (t, len(bad)))

if __name__ == '__main__':
    main()
