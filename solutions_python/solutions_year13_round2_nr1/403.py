def solve(b, n, size):
    if size == 1:
        return str(n)
    l = [n-x for x in range(n+1)]
    i = 1
    while i <= n and b[i-1] < size:
        size += b[i-1]
        b[i-1] = 0
        l[i] = n - i
        i += 1
    while i <= n:
    #    l[i] = n - i
        while size <= b[i-1]:
            size += size - 1
            #print(i,n)
            for k in range(i, n+1):
                l[k] += 1
            
        size += b[i-1]
        i += 1
    #print(str(b))
    #print(str(l))
    #print(min(l))
    #print('---------------------')
    return str(min(l))

f = open('A-large.in')
g = open('A-large.out', 'w')
numcases = int(f.readline())
for casenum in range(1,numcases+1):
    list1 = f.readline().split()
    size = int(list1[0])
    n = int(list1[1])
    #board = []
    #for i in range(0,n):
    board = [int(x) for x in f.readline().split()]
    #print(size, n)
    board.sort()
    #print(board)
    g.write('Case #' + repr(casenum) + ': ' + solve(board, n, size) + '\n')
