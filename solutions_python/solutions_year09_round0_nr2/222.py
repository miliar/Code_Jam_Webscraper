#! /usr/bin/python

import sys
import copy

class Cell:
  def __init__(self, height, row, col):
    self.height = height
    self.row = row
    self.col = col
    self.is_sink = False
    self.sink_label = ''
    self.flows_to = None
    self.my_sink = None

  def sink(self):
    if self.is_sink:
      return self

    if self.my_sink:
      return self.my_sink
    else:
      self.my_sink = self.flows_to.sink()
      return self.my_sink

class Map:
  def __init__(self, cells):
    self.width = len(cells[0])
    self.height = len(cells)
    self.cells = []
    for row in xrange(0, self.height):
      self.cells.append([])
      for col in xrange(0, self.width):
        cell = Cell(cells[row][col], row, col)
#        cell.is_sink = True # TODO: remove me
#        cell.sink = (row, col) # TODO: remove me
        self.cells[row].append(cell)

  def label_sinks(self):
    return
    label = 'a'
    for row in xrange(0, self.height):
      for col in xrange(0, self.width):
        cell = self.cells[row][col]
        if cell.is_sink:
          cell.sink_label = label
          label = chr(ord(label) + 1)

  def print_sinks(self):
    label = 'a'
    for row in xrange(0, self.height):
      row_labels = []
      for col in xrange(0, self.width):
        cell = self.cells[row][col]
        #print "row: %d col: %d cell: %r" % (cell.row, cell.col, cell)
        sink = cell.sink()
        if not sink.sink_label:
          sink.sink_label = label
          label = chr(ord(label) + 1)
        row_labels.append(sink.sink_label)
      print ' '.join(row_labels)

  def compute_sinks(self):
    for row in xrange(0, self.height):
      for col in xrange(0, self.width):
        self.compute_sink_for(row, col)

  def compute_sink_for(self, row, col):
    cell = self.cells[row][col]
    neighbors = self.neighbors(row, col)
    lowest_neighbor = cell
    for neighor in neighbors:
      if neighor.height < lowest_neighbor.height:
        lowest_neighbor = neighor
    if lowest_neighbor == cell:
      cell.is_sink = True
      cell.flows_to = cell
    else:
      cell.flows_to = lowest_neighbor

  def neighbors(self, row, col):
    neighbors = []
    if row > 0:
      neighbors.append(self.cells[row - 1][col])
    if col > 0:
      neighbors.append(self.cells[row][col - 1])
    if col < (self.width - 1):
      neighbors.append(self.cells[row][col + 1])
    if row < (self.height - 1):
      neighbors.append(self.cells[row + 1][col])
    return neighbors

filename = sys.argv[1]
lines = open(filename).readlines()
num_maps = int(lines.pop(0).strip())
maps = []
case_num = 1
for i in xrange(0, num_maps):
  (h, w) = [int(x) for x in lines.pop(0).strip().split(' ')]
  print "Case #%d:" % case_num
  sys.stdout.flush()
  cells = []
  for row in lines[0:h]:
    cells.append([int(x) for x in lines.pop(0).strip().split(' ')])
  map = Map(cells)

  map.compute_sinks()
  map.label_sinks()
  map.print_sinks()

  case_num += 1
