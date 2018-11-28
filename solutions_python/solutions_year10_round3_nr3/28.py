from sys import stdin

T = int(stdin.readline())

def getmaxsize(board, i, j):
   if board[i][j] > 1:
      return 0
   size = 1
   lastnext = board[i][j]
   while True:
      if i+size >= len(board) or j+size >= len(board[0]):
         break
      ok = False
      lastnext = next = 1-lastnext
      for k in xrange(size+1):
         if board[i+k][j+size] != next:
            break
         next = 1-next
      else:
         next = lastnext
         for k in xrange(size+1):
            if board[i+size][j+k] != next:
               break
            next = 1-next
         else:
            ok = True
      if not ok:
         break
      size = size + 1
   return size


def cut(board):
   M, N = len(board), len(board[0])
   besti = -1
   bestj = -1
   bestsize = 0
   for i in xrange(M):
      for j in xrange(N):
         size = getmaxsize(board, i, j)
         if size > bestsize:
            besti = i
            bestj = j
            bestsize = size
   if bestsize > 0:
      for i in xrange(bestsize):
         for j in xrange(bestsize):
            board[besti+i][bestj+j] = 2
   return bestsize


for i in xrange(T):
   M, N = map(int, stdin.readline().split(' '))
   board = []
   for j in xrange(M):
      board.append([0]*N)
      row = int(stdin.readline(), 16)
      for k in xrange(N):
         board[j][N-k-1] = row%2
         row /= 2

   result = []
   last_size = -1
   size = cut(board)
   while size:
      if last_size != size:
         last_size = size
         result.append([size, 1])
      else:
         result[-1][1] += 1
      size = cut(board)
   print "Case #%s: %s" % (i+1, len(result))
   for r in result:
      print r[0], r[1]
