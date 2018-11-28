data = open('A.in', 'r').read().split('\n')

T = int(data.pop(0))

for t in range(T):
   (N, K) = map(int, data.pop(0).split(' '))
   rWin = False
   bWin = False

   #build table
   board = []
   for i in range(N):
      board.append(data.pop(0))

   #rotate
   rotBoard = [[board[N-j-1][i] for j in range(N)] for i in range(N)]
   rotBoard = [''.join(rotBoard[i]) for i in range(N)]
   
   #gravity
   gravBoard = []
   for i in range(N):
      line = ''.join([ln[i] for ln in rotBoard])
      line = line.replace('.', '')
      line = '.' * (N - len(line)) + line
      gravBoard.append(line)

   finBoard = [''.join([ln[i] for ln in gravBoard]) for i in range(N)]

   #find k joints

   #find horizontal
   for line in finBoard:
      if 'R' * K in line:
         rWin = True
      if 'B' * K in line:
         bWin = True

   #find vertical
   if not (rWin and bWin):
      for i in range(N):
         line = ''.join([ln[i] for ln in finBoard])
         if 'R' * K in line:
            rWin = True
         if 'B' * K in line:
            bWin = True

   #find diagonal
   #rotate one
   if not (rWin and bWin):
      rlBoard = []
      for i in range(N):
         line = finBoard[i]
         for j in range(N-i-1):
            line = '.' + line[:-1]
         rlBoard.append(line)

      for i in range(N):
         line = ''.join([ln[i] for ln in rlBoard])
         if 'R' * K in line:
            rWin = True
         if 'B' * K in line:
            bWin = True

   #rotate other
   if not (rWin and bWin):
      rlBoard = []
      for i in range(N):
         line = finBoard[i]
         for j in range(N-i-1):
            line = line[1:] + '.'
         rlBoard.append(line)

      for i in range(N):
         line = ''.join([ln[i] for ln in rlBoard])
         if 'R' * K in line:
            rWin = True
         if 'B' * K in line:
            bWin = True


   if rWin and bWin:
      print 'Case #' + str(t+1) + ': Both'      
   elif rWin:
      print 'Case #' + str(t+1) + ': Red'
   elif bWin:
      print 'Case #' + str(t+1) + ': Blue'
   else:
      print 'Case #' + str(t+1) + ': Neither'
