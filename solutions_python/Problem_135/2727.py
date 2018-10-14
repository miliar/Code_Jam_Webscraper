#!usr/bin/python -tt

import sys

def readboard():
  board = []
  for i in range(0,4):
    board.append(sys.stdin.readline().split())
  return board

def getline(board,ans):
  return board[ans-1]
   
def solve(line1, line2):
  solution = []
  for i in range(0,4):
    if line2[i] in line1:
      solution.append(line2[i])
  if len(solution) == 0:
    return 'Volunteer cheated!'
  elif len(solution) == 1:
    return solution[0]
  else:
    return 'Bad magician!'  

def main():
  numcases = int(sys.stdin.readline())
  for casenum in range(1,numcases+1):
    # first board
    ans1 = int(sys.stdin.readline())
    board1 = readboard()
    line1 = getline(board1,ans1)
    # second board
    ans2 = int(sys.stdin.readline())
    board2 = readboard()
    line2 = getline(board2,ans2)
    print 'Case #' + repr(casenum) + ': ' + solve(line1,line2)

if __name__=='__main__':
  main()
