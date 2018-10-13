#!/usr/bin/python3
import sys
import math
import fractions
from array import array

def rl(convert=''):
  line = sys.stdin.readline().split()  
  for i,c in enumerate(convert):
    if c=='i':
      line[i]=int(line[i])
    elif c=='s':
      pass
    elif c=='f':
      line[i]=float(line[i])
  if len(line)==1:
    line = line[0]
  return line

def gcd(*args):  
  if len(args)==0:
    return 0
  g = args[0]
  for i in range(1,len(args)):
    g = fractions.gcd(g,args[i])    
  return g

def lcm(*args):
  if len(args)==0:
    return 0
  g = args[0]
  for i in range(1,len(args)):
    g *= args[i]  
  return g/gcd(*args)


#--------------------------------------------------------------------#

def load():
  boardX = list()
  boardO = list()
  for i in range(4):
    s = sys.stdin.readline().strip()    
    boardX.append(s.replace('T','X'))
    boardO.append(s.replace('T','O'))
  sys.stdin.readline()
  return boardX, boardO


n = rl('i')
for index in range(n):
  state = None
  bX,bO = load()
  bXT = [''.join(j) for j in map(list,zip(*bX))]
  bOT = [''.join(j) for j in map(list,zip(*bO))]
  bXD =  ''.join([list(bX[i])[i] for i in range(4)])
  bOD =  ''.join([list(bO[i])[i] for i in range(4)])
  bXDT = ''.join([list(bX[i])[3-i] for i in range(4)])
  bODT = ''.join([list(bO[i])[3-i] for i in range(4)])

  # print(bXD, bOD, bXDT, bODT)

  if not state and 'XXXX' in bX or 'XXXX' in bXT or 'XXXX' == bXD or 'XXXX'==bXDT:
    state = 'X won'    
  if not state and 'OOOO' in bO or 'OOOO' in bOT or 'OOOO' == bOD or 'OOOO'==bODT:
    state = 'O won'

  import itertools
  b = list(itertools.chain(*bX))
  if not state and '.' in b:
    state = 'Game has not completed'

  if not state:
    state = 'Draw'

  print('Case #%(index)d: %(state)s' % {'index':index+1, 'state':state})

