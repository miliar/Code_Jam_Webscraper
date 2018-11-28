# encoding: utf-8
import sys

def possible(lawn):
    rows = len(lawn)
    cols = len(lawn[0])
    for r in xrange(0, rows):
        for c in xrange(0, cols):
            val = lawn[r][c]
            
            h = True
            for j in xrange(0, cols):
                if lawn[r][j] > val:
                    h = False
                    break
            
            v = True
            for i in xrange(0, rows):
                if lawn[i][c] > val:
                    v = False
                    break
            
            if not h and not v:
                return 'NO'
    return 'YES'

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for t in xrange(1, T+1):
        line = sys.stdin.readline().rstrip().split()
        n = int(line[0])
        m = int(line[1])
        lawn = []
        for r in xrange(0, n):
            line = sys.stdin.readline().rstrip().split()
            lawn.append([int(x) for x in line])
        ans = possible(lawn)
        print 'Case #%d: %s' % (t, ans)