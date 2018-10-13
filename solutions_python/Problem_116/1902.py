#!/usr/bin/python

infile = open('A-large.in')
outfile = open('ox_out', 'w')
num_case = int(infile.readline())
def or_func(x, y):
  return x or y
for i in range(1, num_case + 1):
  o = [ [ False ] * 4 for j in range(4) ]
  x = [ [ False ] * 4 for j in range(4) ]
  board_full = True
  for j in range(4):
    line = infile.readline()
    for k in range(4):
      if line[k] == 'O':
        o[j][k] = True
      elif line[k] == 'X':
        x[j][k] = True
      elif line[k] == 'T':
        o[j][k] = True
        x[j][k] = True
      elif line[k] == '.':
        board_full = False
  infile.readline()
  orow = [ True ] * 4
  ocol = [ True ] * 4
  odiag = [ True ] * 2
  xrow = [ True ] * 4
  xcol = [ True ] * 4
  xdiag = [ True ] * 2
  for j in range(4):
    for k in range(4):
      orow[j] = orow[j] and o[j][k]
      ocol[k] = ocol[k] and o[j][k]
      xrow[j] = xrow[j] and x[j][k]
      xcol[k] = xcol[k] and x[j][k]
      if j == k:
        odiag[0] = odiag[0] and o[j][k]
        xdiag[0] = xdiag[0] and x[j][k]
      elif j + k == 3:
        odiag[1] = odiag[1] and o[j][k]
        xdiag[1] = xdiag[1] and x[j][k]
  owin = reduce(or_func, orow, False) or reduce(or_func, ocol, False) or reduce(or_func, odiag, False)
  xwin = reduce(or_func, xrow, False) or reduce(or_func, xcol, False) or reduce(or_func, xdiag, False)
  if owin:
    result = 'Case #' + str(i) + ': O won'
  elif xwin:
    result = 'Case #' + str(i) + ': X won'
  elif board_full:
    result = 'Case #' + str(i) + ': Draw'
  else:
    result = 'Case #' + str(i) + ': Game has not completed'
  outfile.write(result + '\n')
