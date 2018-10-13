#!/usr/bin/python
from pprint import pprint
import string

#----------------------------------------------------------------------
# Input
#----------------------------------------------------------------------
FILE = 'A-small'

class Reader:
  def __init__(self, filename):
    self.c = -1
    self.lines = open(filename + '.in').read().split('\n')

  def get(self):
    self.c += 1
    return self.lines[self.c]

  def get_number(self):
    return string.atoi(self.get())

r = Reader(FILE)
tasks = []
n = r.get_number()

for i in range(n):
  s = r.get_number()
  engines = []
  for j in range(s):
    engines.append(r.get())
  q = r.get_number()
  queries = []
  for j in range(q):
    queries.append(r.get())
  tasks.append({'engines': engines, 'queries': queries})

#----------------------------------------------------------------------
# Business Logic
#----------------------------------------------------------------------

def count_jumps(engines, queries):
  jumps = []
  for q in range(len(queries)):
    longest = 0
    for i in range(len(engines)):
      for j in range(q, len(queries)):
        if queries[j] == engines[i]: break
        if j - q + 1 > longest: longest = j - q + 1
    jumps.append(longest)
  return jumps

class Tracker:
  def __init__(self, jumps):
    self.jumps = jumps
    self.length = len(jumps)
    self.best = [1] * self.length
    self.visited = []

  def track(self, index = 0, path = []):
    if index in self.visited: return
    self.visited.append(index)
    if sum(path) >= self.length:
      self.check_best(path)
    else:
      if len(path) >= len(self.best) - 1: return
      c = self.jumps[index]
      for i in range(c, 0, -1):
        self.track(index + i, path + [c])
    
  def check_best(self, path):
    if len(path) < len(self.best):
      self.best = path
    
  def get_result(self):
    if self.best == []: return 0
    return len(self.best) - 1

#----------------------------------------------------------------------
# Output
#----------------------------------------------------------------------
f = open(FILE + '.out', 'w')

i = 0
for task in tasks:
  i += 1

  jumps = count_jumps(task['engines'], task['queries'])
  tracker = Tracker(jumps)
  tracker.track()

  f.write('Case #' + str(i) + ': ')
  f.write(str(tracker.get_result()))
  f.write('\n')

f.close()

