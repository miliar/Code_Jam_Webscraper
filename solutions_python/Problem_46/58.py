f = open('q1.txt')
T = int(f.readline())

t = 0
while t != T:
    t += 1
    N = int(f.readline())
    matrix = [list(map(int, list(f.readline().strip()))) for x in range(N)]
    swaps = 0
    
    for n in range(N-1):
      # for x in matrix:
       #    print(x)
      # print()
       r = list(row for row in range(n, N) if not any(matrix[row][n+1:]))
     #  print (r)
       if n not in r:
           swaps += r[0]-n
           for x in range(r[0]-1, n-1, -1):
               matrix[x], matrix[x+1] = matrix[x+1], matrix[x]
        
    print('Case #%d: %d' % (t,swaps))
