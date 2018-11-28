infile = 'D-small-attempt1.in'
outfile = 'D-small-out.txt'

import math

def main():
  out = open(outfile, 'w')
  f = open(infile)
  N = int(f.readline())
  for n in xrange(N):
    [X, R, C] = [int(i) for i in f.readline().split()]
    winner = ''
    if R*C % X != 0: 
      winner = "RICHARD"
    elif X == 4:
      if R*C <= 8:
        winner = "RICHARD"
    elif X == 3:
      if R*C == 3:
        winner = "RICHARD"
    if winner == '':
      winner = "GABRIEL"
    out.write("Case #"+str(n+1)+": "+winner+"\n")


main()

