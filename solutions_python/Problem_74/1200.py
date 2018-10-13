def solve(moves):
  b_pos, b_moves = 1, []
  o_pos, o_moves = 1, []
  cycle = 0
  for move in moves:
    if move[0] == "B": b_moves.append(move[1])
    else: o_moves.append(move[1])
  while moves:
    push = False
    cycle += 1
    player, target = moves[0]
    if b_moves:
      if b_pos == b_moves[0]:
        if player == "B":
          b_moves = b_moves[1:]
          push = True
      else:
        if b_pos > b_moves[0]: b_pos -= 1
        else: b_pos += 1
    if o_moves:
      if o_pos == o_moves[0]:
        if player == "O":
          o_moves = o_moves[1:]
          push = True
      else:
        if o_pos > o_moves[0]: o_pos -= 1
        else: o_pos += 1
    if push:
      moves = moves[1:]

      
    
  return cycle
    

if __name__ == "__main__":
  t = int(raw_input().strip())
  for i in xrange(1, t+1):
    case = raw_input().split()
    n = case[0]
    j = 2
    moves = []
    while j < len(case):
      moves.append((case[j-1], int(case[j])))
      j += 2
    print "Case #%d: %d" % (i, solve(moves))
