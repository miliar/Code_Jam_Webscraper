import sys, math, re

        



def main():
#    inFile = sys.__stdin__
#    outFile = sys.__stdout__
    inFile = open('B-large.in', 'rt')
    outFile = open(inFile.name.replace('.in', '.out'), 'wt')
    T = int(inFile.readline())
    for t in xrange(1,T+1):
        tt = inFile.readline().strip().split(' ')
#        print '------------------', tt
        tt.reverse()
        C = int(tt.pop())
        c = [tt.pop() for _ in xrange(C)]
        D = int(tt.pop())
        d = [tt.pop() for _ in xrange(D)]
        N = int(tt.pop())
        seq = list(tt.pop())
        out = ''
        cc = []
        for s in c:
            a,b,c = s
            expr = re.compile('(%s%s|%s%s)$' % (a,b,b,a))
            cc.append((expr, c))
        dd = []
        for s in d:
            a,b = s
            expr = re.compile('(%s.*?%s)|(%s.*?%s)' % (a,b,b,a))
            dd.append(expr)
        for s in seq:
            out += s
            for e, s in cc:
                out, n = e.subn(s, out, 1)
            for e in dd:
                if e.search(out):
                    out = ''
                    break
        
        outFile.write('Case #%d: [%s]\n' % (t, ', '.join(out)))

if __name__ == '__main__':
    main()
