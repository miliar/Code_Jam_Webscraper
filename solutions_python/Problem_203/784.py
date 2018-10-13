def solve(cake, letters):
  if len(letters) == 0:
    for row in cake:
      for ch in row:
        if ch == '?':
          return None
    return cake
  ltr, row, col = letters[0]
  top = bot = row
  left = rite = col
  for top in range(row)[::-1]:
    if cake[top][col] != '?': break
  for bot in range(row+1, len(cake)):
    if cake[bot][col] != '?': break
  for left in range(col)[::-1]:
    if cake[row][left] != '?': break
  for rite in range(col+1, len(cake[0])):
    if cake[row][rite] != '?': break
  for start_row in range(top, row+1):
    for stop_row in range(row, bot+1):
      for start_col in range(left, col+1):
        for stop_col in range(col, rite+1):
          no_room = False
          for r in range(start_row, stop_row+1):
            for c in range(start_col, stop_col+1):
              if (r,c) != (row,col) and cake[r][c] != '?':
                no_room = True
                break
            if no_room: break
          if no_room: break
          cake2 = cake[:]
          for r in range(start_row, stop_row+1):
            cake2[r] = cake[r][:start_col] + ltr*(stop_col-start_col+1) + cake[r][stop_col+1:]
          sol = solve(cake2, letters[1:])
          if sol is not None: return sol
for t in range(1,input()+1):
  r, c = map(int, raw_input().split())
  cake = []
  for i in range(r):
    cake += [raw_input()]
  letters = [(ch,r,c) for r,row in enumerate(cake) for c,ch in enumerate(row) if ch != '?']
  print 'Case #%i:'%t
  for row in solve(cake, letters): print row
