#!/usr/bin/env python

import os, numpy, math, sys, string

def check_row(inpData):
  for i in range(1, len(inpData)):
    if inpData[i]=='T': inpData[i]=inpData[i-1]
    if inpData[i-1]=='T': inpData[i-1]=inpData[i]

    if (inpData[i]<>inpData[i-1]): return "fail"
  return inpData[i]

infile = open(sys.argv[1],"r")
lines = infile.readlines()
infile.close()

T=int(lines[0])
output = ''

for t in range(0,T):
  table = []
  for c in range(0,4):
    line=lines[t*4+c+1+t].strip().split()
    table.append(line)
  #check horizontals:
  X = False;
  O = False; 
  for c in range(0, 4):
    # Check horizont
    res = check_row([table[c][0][0], table[c][0][1], table[c][0][2],table[c][0][3]])  
    if res=='O': O = True
    elif res=='X': X = True

    # Check vertical
    res = check_row([table[0][0][c], table[1][0][c], table[2][0][c],table[3][0][c]])  
    if res=='O': O = True
    elif res=='X': X = True
  
  res = check_row([table[0][0][0], table[1][0][1], table[2][0][2],table[3][0][3]])  
  if res=='O': O = True
  elif res=='X': X = True
  
  res = check_row([table[3][0][0], table[2][0][1], table[1][0][2],table[0][0][3]])  
  if res=='O': O = True
  elif res=='X': X = True
  
  resOutput = ''
  if (O): resOutput = "O won"
  elif (X): resOutput = "X won"
  else:
      for i in range (0,4):
        for z in range (0, 4):
          if table[i][0][z] == '.': resOutput = "Game has not completed"
      if resOutput=='': resOutput = "Draw"

  output += 'Case #%d: %s\n' % (t+1, resOutput)

print output
file(sys.argv[1]+'.res','w').write(output)
