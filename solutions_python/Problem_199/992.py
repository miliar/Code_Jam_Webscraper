# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:23:21 2017

@author: John
"""

cases = int(input())
for case in range(cases):
  word, size = input().split()
  size = int(size)
  flips = 0
  impossible = False
  word = [letter for letter in word]
  for i in range(len(word)):
    char = word[i]
    #print("Iteration {}, word is {}".format(i, word))
    if char == "-":
      if i + size > len(word):
        impossible = True
      else:
        for spot in range(i, i + size):
          #print("At spot {}, char is {}".format(spot, word[spot]))
          if word[spot] == "-":
            word[spot] = "+"
          else:
            word[spot] = "-"
        flips += 1
    if impossible:
      print("Case #{}: IMPOSSIBLE".format(case + 1))
      break
  if not impossible:
    print("Case #{}: {}".format(case + 1, flips))
      