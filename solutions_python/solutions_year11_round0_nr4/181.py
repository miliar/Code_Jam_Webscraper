
import random, copy
from functools import *
import itertools
import math

class Array:
  def __init__(self, array):
    self.unsort_array = array
    self.sort_array = copy.copy(self.unsort_array)
    self.sort_array.sort()
    self.unsort_graph = {}
    for i, value in enumerate(self.sort_array):
      self.unsort_graph[value] = i
    self.marked_array = len(self.unsort_array)*[False]
  
  def max_cycle(self):
    return max(list(map(lambda x: self.count_cycle(x), range(0, len(self.unsort_array)))))
      
  def count_cycle(self, starting_pos):
    cycle_size = 1
    current_pos = self.unsort_graph[ self.unsort_array[starting_pos] ]
    while starting_pos != current_pos:
      cycle_size += 1
      current_pos = self.unsort_graph[ self.unsort_array[current_pos] ]
    return cycle_size
    
  def mark_cycle(self, starting_pos):
    current_pos = self.unsort_graph[ self.unsort_array[starting_pos] ]
    self.marked_array[ starting_pos ] = True
    while starting_pos != current_pos:
      self.marked_array[ current_pos ] = True
      current_pos = self.unsort_graph[ self.unsort_array[current_pos] ]

random.seed()

#stomps = 0
#ct = 10000
#for i in range(0, ct):
#  a = Array( [1,2,3] )
#  while a.max_cycle() != len(a.unsort_array):
#    random.shuffle( a.unsort_array )
#    a = Array( a.unsort_array )
#  while a.max_cycle() == len(a.unsort_array):
#    stomps += 1
#    random.shuffle( a.unsort_array )
#    a = Array( a.unsort_array )
#print(stomps / ct)
# 2 cycle - 2 / 1
# 3 cycle - 3 / 2
# 4 cycle - 4 / 3
# 5 cycle - 5 / 4
# 6 cycle - 6 / 5

def step_cost(cycles):
  if cycles == 1:
    return 0
  else:
    return cycles / (cycles-1)

def total_cost(cycles):
  if cycles == 1:
    return 0
  else:
    return cycles

cycle_cost = []
cycle_cost.append(0)

for i in range(2,8):
  permutes = range(0,i)
  cost = 0
  ct = 0
  cycle_counts = len(permutes)*[0]
  
  for p in itertools.permutations(permutes):
    max_cycle = Array( list(p) ).max_cycle()
    cycle_counts[max_cycle-1] += 1
    if max_cycle == len(permutes):
      continue
    cost += cycle_cost[max_cycle-1] + step_cost(len(permutes))
    ct += 1
    
  print(cycle_counts)
  cycle_cost.append( cost / ct )

print(cycle_cost)

from functools import *
import copy
data = open("D-large.in", "r")
myout = open("goro_out.txt", "w")
cases = int( data.readline() )

for ct in range(0, cases):
  array_size = int( data.readline() )
  array = Array( list(map( lambda x: int(x), data.readline().split() ) ) )

  stomps = 0
  for i in range(0, len(array.unsort_array)):
    if array.marked_array[i] == True:
      continue
    stomps += total_cost(array.count_cycle(i))
    array.mark_cycle(i)
    
  #myout.write("Case #" + str(ct+1) + str(unsort_array) + '\n')
  myout.write("Case #" + str(ct+1) + ": " + str(stomps) + '\n')
