#!/usr/bin/env python

class basin():
  H = 0
  W = 0
  cells = []
  direction_transform = {'n': (-1, 0), 's': (1, 0), 'w': (0, -1), 'e': (0, 1)}
  cache = {}

  def __init__(self, rows):
    self.H = len(rows)
    self.cells = []
    self.cache = {}
    for i in range(0, len(rows)):
      self.cells.append([])
      data = rows[i].split(" ")
      self.W = len(data)
      for j in range(0, self.W):
        self.cells[i].append(int(data[j]))

  def dest(self, R, C):
    if self.cache.has_key((R,C)):
      return self.cache[(R,C)]

    max_alt = 100000
    alt = {}

    for (dir, tf) in self.direction_transform.iteritems():
       nR = R + tf[0]
       nC = C + tf[1]
       if nR < 0 or nR > self.H-1 or nC < 0 or nC > self.W-1:
         alt[dir] = max_alt
       else:
         alt[dir] = self.cells[nR][nC]

    min_alt = min([x[1] for x in alt.iteritems()])

    if min_alt >= self.cells[R][C]:
      self.cache[(R,C)] = (R, C)
      return (R, C)

    for dir in ('n', 'w', 'e', 's'):
      if alt[dir] == min_alt:
        tf = self.direction_transform[dir]
        nR = R + tf[0]
        nC = C + tf[1]
        result = self.dest(nR, nC)
        self.cache[(R,C)] = result
        return result

  def find_dests(self):
    result = []
    for i in range(0, self.H):
      result.append([])
      for j in range(0, self.W):
        result[i].append(self.dest(i,j))
    return result


  def find_labels(self):
    letters = tuple('abcdefghijklmnopqrstuvwxyz')
    labels = {}
    dests = self.find_dests()
    result = [[''] * self.W for x in range(0,self.H)]
    
    for i in range(0, self.H):
      for j in range(0, self.W):
        if labels.has_key(dests[i][j]):
           label = labels[dests[i][j]]
        else:
           label = letters[len(labels)]
           labels[dests[i][j]] = label
        result[i][j] = label
    
    return result
        

def print_basin(rows):
  bs = basin(rows)
  labels = bs.find_labels()
  for line in labels:
    print ' '.join(line)

input = open("B-large.in", "r")
lines = input.readlines()

ln = 1
case = 1
while ln < len(lines):
  H = int(lines[ln].split(' ')[0])
  bs_lines = []
  for i in range(1, H + 1):
    bs_lines.append(lines[ln + i].strip('\n'))
  print "Case #" + str(case) + ":"
  print_basin(bs_lines)
  case += 1

  ln += H + 1
