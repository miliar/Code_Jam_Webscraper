import sys, math, re

def xor(l): 
    return reduce(lambda x,y: x^y, l)

def main():
#    inFile = sys.__stdin__
#    outFile = sys.__stdout__
    inFile = open('C-large.in', 'rt')
    outFile = open(inFile.name.replace('.in', '.out'), 'wt')
    T = int(inFile.readline())
    for t in xrange(1,T+1):
        N = int(inFile.readline())
        C = map(int, inFile.readline().strip().split(' '))
        if xor(C):
            outFile.write('Case #%d: NO\n' % t)
        else:
            C.sort()
            del C[0]
            outFile.write('Case #%d: %d\n' % (t,sum(C)))
        

if __name__ == '__main__':
    main()
