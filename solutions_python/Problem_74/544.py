#!/usr/bin/python

from sys import stdin

class State:
  def __init__(self):
    self.t   = 0
    self.pos = 1

  def step(self, dist, t):
    time = abs(dist - self.pos)
    self.pos = dist
    self.t = max(self.t + time, t) + 1
    return self.t

def evaluate_case(case):
  opcodes = case.split(' ')
  number = int(opcodes[0])
  opcodes = opcodes[1:2*number+1]

  t = 0
  bot = {'O': State(), 'B': State()}

  for i in range(number):
    t = bot[opcodes[2 * i]].step(int(opcodes[2 * i + 1]), t)

  return str(t)
    
cases = stdin.readlines()
count = int(cases[0])

t = 0

for i in range(1, count+1):
  print('Case #' + str(i) + ': ' + evaluate_case(cases[i]))
