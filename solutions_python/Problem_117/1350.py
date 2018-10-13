

with open('B.in', 'r') as fin:
  with open('B.out', 'w') as fout:
    lines = fin.readlines()
    lidx = 0
    T = int(lines[lidx])
    lidx += 1
    for case in range(T):
      # read in N and M
      N, M = tuple(lines[lidx].split())
      rows = int(N)
      cols = int(M)
      lidx += 1
      board = []
      for i in range(rows):
        board.append(map(int,lines[lidx + i].strip().split()))
      lidx += rows
      #print board

      # Find the min and max for the row
      rowmin = [(101, -1, -1)] * rows
      rowmax = [(-1, -1, -1)] * rows
      colmin = [(101, -1, -1)] * cols
      colmax = [(-1, -1, -1)] * cols
      for row in range(rows):
        for col in range(cols):
          # Rows
          if board[row][col] < rowmin[row][0]:
            rowmin[row] = (board[row][col], row, col)
          if board[row][col] > rowmax[row][0]:
            rowmax[row] = (board[row][col], row, col)
          # Cols
          if board[row][col] < colmin[col][0]:
            colmin[col] = (board[row][col], row, col)
          if board[row][col] > colmax[col][0]:
            colmax[col] = (board[row][col], row, col)

##      print 'rowmin', rowmin
##      print 'rowmax', rowmax
##      print 'colmin', colmin
##      print 'colmax', colmax

      # Iterate over all cells. If lower than the maximum for the col,
      # had to have been mowed along the row. Therefore must be the maximum for the row.
      valid = True
      for row in range(rows):
        if valid:
          for col in range(cols):
            val = board[row][col]
            if val < colmax[col][0] and val != rowmax[row][0]:
              valid = False
              break
            if val < rowmax[row][0] and val != colmax[col][0]:
              valid = False
              break
            

      # Iterate over all minimums and check that it's also the maximum
##      valid = True
##      for cell in rowmin:
##        val, row, col = cell
##        if val != rowmax[row][0] and val != colmax[col][0]:
##          print 'BREAKER:', cell
##          valid = False
##          break
##
##      if valid:
##        for cell in colmin:
##          val, row, col = cell
##          if val != rowmax[row][0] and val != colmax[col][0]:
##            valid = False
##            break

      if valid:
        fout.write('Case #%d: YES\n' % (case+1))
      else:
        fout.write('Case #%d: NO\n' % (case+1))
        
