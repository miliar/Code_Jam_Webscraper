def solve(**kwargs):
  
  board = kwargs['board']
  
  emptyCell = False
  
  steps = [(1,0),(0,1),(1,1),(-1,1)]
  
  for step in steps:
    i = 0
    while i < len(board):
      o = 0
      while o < len(board[i]):
	if board[i][o] == '.':
	  emptyCell = True
	try:
	  flag = True
	  for u in range(4):
	    flag = flag and board[i + u * step[0]][o + u * step[1]] in ('X','T')
	  if flag:
	    return 'X won'
	  flag = True
	  for u in range(4):
	    flag = flag and board[i + u * step[0]][o + u * step[1]] in ('O','T')
	  if flag:
	    return 'O won'
	except IndexError:
	  pass
	o += 1
      i +=1

  return 'Game has not completed' if emptyCell else 'Draw'
    

if __name__ == "__main__":
  
  f_in = open('file.in','r')
  f_out = open('file.out','w')

  T = int(f_in.readline())

  for i in range(T):
    
    problem = {}
    
    problem['board'] = []
    
    for o in range(4):
      problem['board'].append([t for t in f_in.readline().replace('\n','')])
    
    f_in.readline()
  
    f_out.write('Case #' + str(i + 1) + ': ' + solve(**problem) + '\n')

  f_in.close()
  f_out.close