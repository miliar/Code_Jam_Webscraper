import fileinput 
import sets

def main(): 
  inputfile = open('A-small-attempt0.in')

  T = int(inputfile.next())
  # print T

  for case in range(0, T):
    ans1 = int(inputfile.next())
    board = []
    
    for linenum in range(0, 4):
      line = inputfile.next().rstrip().split(" ")
      board.append([int(i) for i in line])
    
    ans2 = int(inputfile.next())
    
    board2 = []
    
    for linenum in range(0, 4):
      line = inputfile.next().rstrip().split(" ")
      board2.append([int(i) for i in line])

    l1 = sets.Set(board[ans1 - 1])
    l2 = sets.Set(board2[ans2 - 1])

    matching = list(l1.intersection(l2))

    print 'Case #' + str(case + 1) + ': ',
    if len(matching) is 1:
      print matching[0]
    elif len(matching) is 0:
      print 'Volunteer cheated!'
    else:
      print 'Bad magician!'

    # for l in board:
    #   print l
  # for case in fileinput.input():

  return

if __name__ == '__main__':
  main()