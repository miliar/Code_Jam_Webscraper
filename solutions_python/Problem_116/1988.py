import sys
def emptyslot(board):
  for i in range(4):
    c = [x for x in board[i] if x == '.']
    if c : return True
  return False
def sat(inchar, winchar) :
  if inchar == 'T' or inchar == winchar : return True
  else : return False
def wins(board , char):
  #check all the rows
  for i in range(4) :
   [a,b,c,d] = board[i]
   if sat(a,char) and sat(b,char) and sat(c,char) and sat(d,char): return True
  #check all columns
  for i in range(4) :
   [a,b,c,d] = [board[0][i], board[1][i], board[2][i], board[3][i]]
   if sat(a,char) and sat(b,char) and sat(c,char) and sat(d,char): return True
  #check the two diagonals
   [a,b,c,d] = [board[0][0], board[1][1], board[2][2], board[3][3]]
   if sat(a,char) and sat(b,char) and sat(c,char) and sat(d,char): return True
   [a,b,c,d] = [board[0][3], board[1][2], board[2][1], board[3][0]]
  if sat(a,char) and sat(b,char) and sat(c,char) and sat(d,char): return True
   
def main():
  f = open("tictactomek.in", "r")
  input = []
  for line in f :
    line = line.strip()
    input.append(line)
  #print input
  #sys.exit(0)
  numtests = int(input.pop(0))
  #input.pop(-1)
  #print input
  #sys.exit(0)
  output = []
  for i in range(numtests):
    board = []
    result = ''
    for k in range(4):
      line = input[k]
      #print line
      [a,b,c,d] = [c for c in line]
      board.append([a,b,c,d])
    del input[:4]
    input.pop(0) 
    #print board
    if not result:
      if wins(board, 'X') : result = 'X won'
      elif wins(board, 'O'): result = 'O won'
      elif emptyslot(board): result = 'Game has not completed'
      else: result = 'Draw'
    output.append(result)
  for i in range(len(output)):
    print 'Case #%d: %s' %(i+1 , output[i])
  sys.exit(0)

if __name__ == '__main__':
  main()
     
