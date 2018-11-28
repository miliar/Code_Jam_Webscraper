def do_magikz(output, num, row, first_board, row_b, second_board):
  res = set(first_board[row-1]).intersection(set(second_board[row_b-1]))
  case = "Case #%s: " % num
  if len(res) == 1:
      output.write(case + str(res.pop()) + "\n")
  elif len(res) == 0:
      output.write(case + "Volunteer cheated!" + "\n")
  elif len(res) > 1:
    output.write(case + "Bad magician!" + "\n")

def main():
  output = open('output.txt','w')
  with open('sample.in','r') as f:
    num_test_cases = int(f.readline())
    for t in range(num_test_cases):
      first_board = []
      row = int(f.readline())
      for r in range(4):
        first_board.append([int(x) for x in f.readline().split()])
      row_b = int(f.readline())
      second_board= []
      for r in range(4):
        second_board.append([int(x) for x in f.readline().split()])
      do_magikz(output, t+1, row, first_board, row_b, second_board)

if __name__ == '__main__':
  main()
