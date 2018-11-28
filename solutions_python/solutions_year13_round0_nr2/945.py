import sys

def testHeight(pattern, h, N, M):
    nbInRow, nbInCol = [0] * N, [0] * M
    for i in range(N):
        for j in range(M):
            if pattern[i][j] == h:
                nbInRow[i] += 1
                nbInCol[j] += 1
                
    for i in range(N):
        for j in range(M):
            if pattern[i][j] == h and (nbInRow[i] < M and nbInCol[j] < N):
                return False
            if pattern[i][j] == h:
                pattern[i][j] = h + 1
        
    return True

def processCase():
    N, M = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    pattern = []
    for i in range(N):
        pattern.append([int(x) for x in sys.stdin.readline().strip().split(' ')])
        
    maxHeight = max([el for row in pattern for el in row])
    for h in range(1, maxHeight + 1):
        if not testHeight(pattern, h, N, M):
            return 'NO'
    
    return 'YES'

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        result = processCase()
        print 'Case #%d: %s' % (i + 1, result)
        
if __name__ == '__main__':
    main()
