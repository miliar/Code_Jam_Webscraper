INPUT_FILE = "test_input.in"

class Found(Exception):
  pass

def generate(case_file):
  n_cases = int(case_file.readline())
  boards = []
  for n_boards in range(n_cases):
    board = []
    for i in range(4):
      tmp_line = []
      tmp_line = list(case_file.readline().strip())
      board.append(tmp_line)
    case_file.readline()
    boards.append(board)
  return parse_graph(boards)

def parse_graph(boards):
  for i,board in enumerate(boards):
    algo(board,i+1)

def algo(board, n_case):
  # check rows
  try: 
    for i,line in enumerate(board):
      same = 0
      for k,row in enumerate(line):
        if k !=0 and line[k-1] == row and row != '.':
          same += 1
        if same == 3 or same == 2 and row == 'T':
          if line[k-1] == "X":
            print "Case #" + str(n_case) + ": X won"
            raise Found
          if line[k-1] == "O":
            print "Case #" + str(n_case) + ": O won"
            raise Found
    # check columns
    same = 0
    t_board = zip(*board)
    for i,line in enumerate(t_board):
      same = 0
      for k,column in enumerate(line):
        if k !=0 and line[k-1] == column and column != '.':
          same += 1
        if same == 3 or same == 2 and column == 'T':
          if line[k-1] == "X":
            print "Case #" + str(n_case) + ": X won"
            raise Found
          if line[k-1] == "O":
            print "Case #" + str(n_case) + ": O won"
            raise Found
    # check diagonals 
    diagonal = [line[i] for i,line in enumerate(board)]
    same = 0
    for k,column in enumerate(diagonal):
      if k !=0 and diagonal[k-1] == column and column != '.':
        same += 1
      if same == 3 or same == 2 and column == 'T':
        if diagonal[k-1] == "X":
          print "Case #" + str(n_case) + ": X won"
          raise Found
        if diagonal[k-1] == "O":
          print "Case #" + str(n_case) + ": O won"
          raise Found
    diagonal = [line[-i-1] for i,line in enumerate(board)]
    same = 0
    for k,column in enumerate(diagonal):
      if k !=0 and diagonal[k-1] == column and column != '.':
        same += 1
      if same == 3 or same == 2 and column == 'T':
        if diagonal[k-1] == "X":
          print "Case #" + str(n_case) + ": X won"
          raise Found
        if diagonal[k-1] == "O":
          print "Case #" + str(n_case) + ": O won"
          raise Found
    # check draw and game not completed
    for k, column in enumerate(board):
      if column[k] == '.':
        print "Case #" + str(n_case) + ": Game has not completed"
        raise Found

    print "Case #" + str(n_case) + ": Draw"
    raise Found

  except Found:
    pass

def get_cases(case_file):
  generate(case_file)

def main():
  case_file = open(INPUT_FILE,'r')
  cases = get_cases(case_file)

if __name__ == '__main__':
  main()