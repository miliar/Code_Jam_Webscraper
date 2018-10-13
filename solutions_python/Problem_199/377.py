import sys
import array


def main():
    infile = open(sys.argv[1]) if len(sys.argv)>1 else sys.stdin
    T = int(next(infile))
    for case_no in xrange(1, T+1):
        S,K = next(infile).split(' ')
        s = s = array.array('c', S)
        k = int(K)
        print 'Case #%d: %s' % (case_no, solve(s, k))

def solve(s, k):
    flips = 0
    for pos in xrange(len(s)-k+1):
        if s[pos]=='-':
            # flip
            for i in xrange(pos, pos+k):
                s[i] = '-' if s[i]=='+' else '+'
            flips += 1
    #no check whether its ok
    for i in xrange(k):
        if s[-i]=='-':
            return 'IMPOSSIBLE'
    
    return str(flips)

if __name__ == '__main__':
    main()
        