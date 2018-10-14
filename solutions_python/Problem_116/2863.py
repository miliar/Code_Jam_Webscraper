# -*- coding: utf-8 -*-

import numpy

def is_line_winner(tab):
  for l in tab:
    nbx = 0
    nbo = 0
    for l2 in l:
      if l2 == "X":
        nbx += 1
      elif l2 == "O":
        nbo += 1
    if nbx == 4:
      return "X won"
    elif nbo == 4:
      return "O won"
    if (nbx == 3 or nbo == 3):
      for l2 in l:
        if (l2 == "T" and nbo == 3):
          return "O won"
        elif (l2 == "T" and nbx == 3):
          return "X won"


def is_diagonal_winner(tab):

  diag = [[tab[0][0], tab[1][1], tab[2][2], tab[3][3]],[tab[0][3], tab[1][2],
    tab[2][1], tab[3][0]]]
  for i in range(len(diag)):
    nbx = 0
    nbo = 0
    nbt = 0
    for t in diag[i]:
      if t == "X":
        nbx += 1
      elif t == "O":
       nbo += 1
      elif t == "T":
        nbt += 1
    if nbx == 4:
      return "X won"
    elif nbo == 4:
      return "O won"
    elif (nbx == 3 and t == 1):
      return "X won"
    elif (nbo == 3 and t == 1):
      return "0 won"

def is_points(tab):
  for i in tab:
    for j in i:
      if (j == "."):
        return True


def is_tic_tac(tab):
  res = is_line_winner(tab.tolist())
  if (res != None):
    return res
  res = is_line_winner(tab.T.tolist())
  if (res != None):
    return res
  res = is_diagonal_winner(tab.tolist())
  if (res != None):
    return res
  if (is_points(tab.tolist())):
    return("Game has not completed")
  else:
    return ("Draw")


if __name__ == "__main__":
  nbParties = input();
  tab = numpy.zeros(shape=(4,4))
  tab = tab.tolist()
  result = []
  for i in range(nbParties):
    for i in range(4):
      ligne = raw_input();
      for j in range(4):
        tab[i][j] = ligne[j]
    result.append(is_tic_tac(numpy.matrix(tab)))
    raw_input()
  for i in range (nbParties):
    print("Case #" + str(i + 1) + ": " + result[i])



