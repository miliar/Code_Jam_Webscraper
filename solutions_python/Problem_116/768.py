import sys

#Notes: 
#Practice on small snipet before attempting small or large.
#If they ask for indices, they want indices starting at 1
#Can break out of multiple loops if you match for statement with else continue break
#Main parses file and puts it into a dictionary removing end of line characters
#Function is called from there and rememeber to call output from function

out = open('out.txt', 'w')

def main(filename):
  f = open(filename)
  lst = []
  for line in f:
    lst.append(line.rstrip())
  function(lst)

def function(lst):
  #this can change
  #to split string and cast as ints  use: [int(x) for x in lst[case*3 + 2].split(" ")]
  cases = int(lst[0])
  case = 0
  #this while loop iterates through all caseses. Set desired output for the case 
  #equal to line
  while case < cases:
  #enter solution here
    rows = []
    rows.append(list(lst[case*5 + 1]))
    rows.append(list(lst[case*5 + 2]))
    rows.append(list(lst[case*5 + 3]))
    rows.append(list(lst[case*5 + 4]))
    line = winner(rows)
  
  #solution ends here
    case += 1
    output(case, line)

def winner(lst):
  for rw in lst:
    if row(rw, 'X'):
      return "X won"
    if row(rw, 'O'):
      return 'O won'
  if column(lst, 'X') or diagonalL(lst, 'X') or diagonalR(lst, 'X'):
    return 'X won'
  elif column(lst, 'O') or diagonalL(lst, 'O') or diagonalR(lst, 'O'):
    return 'O won'
  for rw in lst:
    if '.' in rw:
      return "Game has not completed"
  return "Draw"

def row(lst, val):
  if lst.count(val) == 4 or (lst.count(val) == 3 and 'T' in lst):
    return True
  return False

def column(matrix, val):
  i = 0
  while i < 4:
    lst = [row[i] for row in matrix]
    if lst.count(val) == 4 or (lst.count(val) == 3 and 'T' in lst):
      return True
    i += 1
  return False

def diagonalL(lst, val):
  current = [lst[0][0], lst[1][1], lst[2][2], lst[3][3]]
  if current.count(val) == 4 or (current.count(val) == 3 and 'T' in current):
    return True
  else:
    return False

def diagonalR(lst, val):
  current = [lst[0][3], lst[1][2], lst[2][1], lst[3][0]]
  if current.count(val) == 4 or (current.count(val) == 3 and 'T' in current):
    return True
  else:
    return False


def output(case, sol):
  string = "Case #" + str(case) + ": " + str(sol) + "\n"
  out.write(string)

if __name__ == "__main__":
  arg = sys.argv[1]
  main(str(arg))
  

