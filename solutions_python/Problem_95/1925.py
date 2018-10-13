#!/usr/bin/env python

def g2emapping(letter):
  if letter == "y":
    eletter = "a"
  elif letter == "n":
    eletter = "b"
  elif letter == "f":
    eletter = "c"
  elif letter == "i":
    eletter = "d"
  elif letter == "c":
    eletter = "e"
  elif letter == "w":
    eletter = "f"
  elif letter == "l":
    eletter = "g"
  elif letter == "b":
    eletter = "h"
  elif letter == "k":
    eletter = "i"
  elif letter == "u":
    eletter = "j"
  elif letter == "o":
    eletter = "k"
  elif letter == "m":
    eletter = "l"
  elif letter == "x":
    eletter = "m"
  elif letter == "s":
    eletter = "n"
  elif letter == "e":
    eletter = "o"
  elif letter == "v":
    eletter = "p"
  elif letter == "z":
    eletter = "q"
  elif letter == "p":
    eletter = "r"
  elif letter == "d":
    eletter = "s"
  elif letter == "r":
    eletter = "t"
  elif letter == "j":
    eletter = "u"
  elif letter == "g":
    eletter = "v"
  elif letter == "t":
    eletter = "w"
  elif letter == "h":
    eletter = "x"
  elif letter == "a":
    eletter = "y"
  elif letter == "q":
    eletter = "z"
  else:
    eletter = " "
  return eletter

fin = open("A-small-attempt0.in.txt")
fout = open("A-small-attempt0.out.txt", "w")

T = int(fin.readline().strip())
for X in range(1,T+1):
  fout.write("Case #" + str(X) + ": ")
  G = fin.readline()
  for j in range(0, len(G)-1):
#    S[j]=g2emapping(G[j])
    fout.write(g2emapping(G[j]))

  fout.write("\n")
#  fout.write("Case #" + str(X) + ": " + S)

fin.close()
fout.close()
