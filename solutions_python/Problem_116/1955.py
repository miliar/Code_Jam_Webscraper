#!/usr/bin/python -O

import sys

def findWinner(line,n_case):
   x = line.count('X')
   o = line.count('O')
   d = line.count('.')
   t = line.count('T')
   if x == 4 or (x == 3 and t == 1):
     print "Case #" + str(n_case) + ': ' + 'X won'
     return True
   if o == 4 or (o == 3 and t == 1):
     print "Case #" + str(n_case) + ': ' + 'O won'
     return True

def main(argv=None):
  if argv is None:
    argv = sys.argv

  try:
    f = open(sys.argv[1], 'r')
  except IndexError as e:
    print "Please specify an input file"
    return 127
  except IOError as e:
    print "Could not read file!"
    return 127

  n = int(f.readline())
  n_case = 1
  row = 1
  m = []
  winner = False
  incomplete = False

  while n_case <= n:
    while row <= 4:
      m.append(list(f.readline().strip()))
      row = row + 1
    #winner moves
    #rows
    for r in m:
      if findWinner(r,n_case):
        winner = True
        break
    if not winner:
      #columns
      q = zip(*m)
      for c in q:
        z = list(c)
        if findWinner(z,n_case):
          winner = True
          break
      #diagonals
      if not winner:
        k = len(m[0])
        d1 = [m[i][i] for i in range(k)]
        d2 = [m[k-1-i][i] for i in range(k-1,-1,-1)]
        if findWinner(d1,n_case) or findWinner(d2,n_case):
          winner = True
    #no winners, check if game has not completed
    if not winner:
      for r in m:
        if '.' in r:
          incomplete = True
          print "Case #" + str(n_case) + ': ' + 'Game has not completed'
          break
      #we have a draw
      if not incomplete:
         print "Case #" + str(n_case) + ': ' + 'Draw'

    n_case += 1
    f.readline()
    winner = False
    incomplete = False
    row = 1
    m = []
  f.close()
  return 0

if __name__ == "__main__":
    sys.exit(main())
