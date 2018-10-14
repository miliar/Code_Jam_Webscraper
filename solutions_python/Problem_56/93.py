import sys, re

def main():
    inFile = open(sys.argv[1], 'rt')
    outFile = open(inFile.name.replace('.in', '.out'), 'wt')
#    outFile = sys.__stdout__
    T = int(inFile.readline())
    for t in xrange(1,T+1):
        N,K = map(int, inFile.readline().strip().split(' '))
        rows = []
        for n in xrange(N):
            l = inFile.readline().strip()
            j = N-1
            while re.match(r'.*[RB].*', l[:j+1]):
                if l[j]=='.':
                    l = '.'+l[:j]+l[j+1:]
                else:
                    j = j-1    
            rows.append(l)
        wins = set()
        for i in xrange(N):
            for j in xrange(N):
                # start looking down, right and diag
                c = rows[i][j]
                if c=='.':
                    continue
                if  check(rows, c, i, j, 1,0, N, K): wins.add(c)
                if  check(rows, c, i, j, 1,1, N, K): wins.add(c)
                if  check(rows, c, i, j, 0,1, N, K): wins.add(c)
                if  check(rows, c, i, j, 1,-1, N, K): wins.add(c)
                if  check(rows, c, i, j, -1,1, N, K): wins.add(c)
        if 'R' in wins and 'B' in wins:
            output = 'Both'             
        elif 'R' in wins:
            output = 'Red'             
        elif 'B' in wins:
            output = 'Blue'
        else:                 
            output = 'Neither'
        outFile.write('Case #%d: %s\n' % (t, output))
       
def check(rows, c, x, y, dx, dy, N, K):
    i = 0
    while x>=0 and x<N and y>=0 and y<N and i<K:
        if rows[x][y]!=c:
            return False
        i += 1
        if i==K:
            return True
        x += dx
        y += dy

if __name__ == '__main__':
    main()
