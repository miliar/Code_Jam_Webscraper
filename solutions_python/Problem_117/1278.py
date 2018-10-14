data = open('b.txt', 'r').read().split('\n')

def test(lawn, maxRows, maxCols, N, M, t):
   for i in range(N):
      for j in range(M):
         if lawn[i][j] < maxRows[i] and lawn[i][j] < maxCols[j]:
            print 'Case #' + str(t+1) + ': NO'
            return

   print 'Case #' + str(t+1) + ': YES'


(T,) = map(int, data.pop(0).split(' '))

for t in range(T):
   (N,M) = map(int, data.pop(0).split(' '))
   lawn = []
   maxRows = {}
   maxCols = {}
   
   for n in range(N):
      lawn.append(map(int, data.pop(0).split(' ')))

   for i in range(N):
      for j in range(M):
         maxRows[i] = max(maxRows.get(i, 0), lawn[i][j])
         maxCols[j] = max(maxCols.get(j, 0), lawn[i][j])

   test(lawn, maxRows, maxCols, N, M, t)