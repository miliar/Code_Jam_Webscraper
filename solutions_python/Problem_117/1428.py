from sys import argv
from lib.File import FileParser

def scan_row(board, row, val):
  rv = True
  valCount = 0
  for num in board[row]:
    rv = rv and (num == val or num == 0)
    if num == val:
      valCount += 1
  return (rv, valCount)

def scan_col(board, col, val):
  rv = True
  valCount = 0
  for j in range(len(board)):
    rv = rv and (board[j][col] == val or board[j][col] == 0)
    if board[j][col] == val:
      valCount += 1
  return (rv, valCount)

def clear_row(board, row):
  for i in range(len(board[row])):
    board[row][i] = 0

def clear_col(board, col):
  for j in range(len(board)):
    board[j][col] = 0

def find(board, val):
  for rownum, row in enumerate(board):
    if val in row:
      return (rownum, row.index(val))

def case_logic(case_args):
  board = []
  vals = case_args[-1]
  for i in range(1, len(case_args)-1):
    board.append(map(int, case_args[i].split()))
  while len(vals.keys()) > 0:
    minVal = min(vals.keys())
    loc = find(board, minVal)
    rowscan = scan_row(board, loc[0], minVal)
    colscan = scan_col(board, loc[1], minVal)
    if rowscan[0]:
      clear_row(board, loc[0])
      vals[minVal] -= rowscan[1]
    elif colscan[0]:
      clear_col(board, loc[1])
      vals[minVal] -= colscan[1]
    else:
      return "NO"
    if vals[minVal] == 0:
      del vals[minVal]
  return "YES"


def main(args):
  parser = FileParser(1, 'dynamic', args[0])
  problem = parser.parse_problem()
  problem.set_case_logic(case_logic)
  problem.solve()
  problem.done()

if __name__ == "__main__":
  main(argv[1:])
