"""
    Problem B. Lawnmower
"""
import sys

def solve(a, M, N):
    greatest_row = [None]*M
    greatest_column = [None]*N
    #sys.stdout.write('a %s\n' % str(a))
    for m in range(M):
        for n in range(N):
            if greatest_row[m] == None:
                greatest_row[m] = a[m][n]
            elif greatest_row[m] < a[m][n]:
                greatest_row[m] = a[m][n]
            if greatest_column[n] == None:
                greatest_column[n] = a[m][n]
            elif greatest_column[n] < a[m][n]:
                greatest_column[n] = a[m][n]
    #sys.stdout.write('row %s\ncolumn %s\n' % (str(greatest_row), str(greatest_column)) )
    for m in range(M):
        for n in range(N):
            if (a[m][n] < greatest_row[m]) and (a[m][n] < greatest_column[n]):
                return 'NO'
    return 'YES'

if  __name__ == '__main__':
    T = int(raw_input()) 
    t = 0 
    while t < T:
        t = t+1
        (M,N) = raw_input().split()[:2]
        M = int(M)
        N = int(N)
        lawn = [None] * M
        #sys.stdout.write('N=%s and M=%s \n' % (N,M) )
        for m in range(M):
            line = raw_input()
            lawn[m] = list(''.join(line.split()))
        answer = solve(lawn, M, N)
        sys.stdout.write('Case #%d: %s\n' % (t, answer) )
