import sys, math

def main():
    inFile = open('B-large.in', 'rt')
    outFile = open(inFile.name.replace('.in', '.out'), 'wt')
#    outFile = sys.__stdout__
    T = int(inFile.readline())
    for t in xrange(1,T+1):
        L,P,C = map(int, inFile.readline().strip().split(' '))
        l = []
        cur = L
        while cur*C<P:
            l.append(cur*C)
            cur *= C
        if len(l):
            res = int(round(math.log(len(l),2)+0.5))
        else:
            res = 0
        outFile.write('Case #%d: %d\n' % (t, res))
    outFile.close()
        

if __name__ == '__main__':
    main()
