#!/usr/bin/python

import sys
import string
import logging
import random
import time

logging.basicConfig(level=logging.INFO)


class Point(object):
  def __init__(self, elev, x, y):
    self.elev = elev
    self.label = None
    self.x = x
    self.y = y
  def __repr__(self):
    return "Point(elev=%d,label=%s)" % (self.elev, self.label)

def work():
  input = file(sys.argv[1])
  for case in range(int(input.readline().strip())):
    height, width = map(int, input.readline().strip().split(" "))
    # logging.info("h %d w %d" % (height, width))
    tabular = []
    for i in range(height):
      tabular.append(map(int, input.readline().strip().split(" ")))
    deal(tabular,height,width, case)

def test():
  height = 100
  width = 100
  tabular= []
  for i in range(height):
    tabular.append([])
    for j in range(width):
      tabular[i].append(random.randint(0,10000))
  start = time.time()
  deal(tabular, 100, 100, 1)
  print "Elapsed:" + str(time.time()-start)


def deal(tabular, height, width, case):  
  mat = {}
  for i in range(height):
    for j in range(width):
      mat[i,j] = Point(tabular[i][j], i, j)

  global cur_label # janky
  cur_label = 0
  def walk(i, j):
    global cur_label # janky!
    this = mat[i, j]
    if this.label:
      return this.label

    north = mat.get((i-1,j), Point(99999, -1, -1))
    west = mat.get((i, j-1), Point(99999, -1, -1))
    east = mat.get((i, j+1), Point(99999, -1, -1))
    south = mat.get((i+1, j), Point(99999, -1, -1))
    all = [ north, west, east, south ]
    elevs = list([ p.elev for p in all ])
    m = min(elevs)
    if m < this.elev:
      ind = elevs.index(m)
      next = all[ind]
      this.label = walk(next.x, next.y)
      # logging.info("%d %d %s" % (this.x, this.y, this.label))
      return this.label
    else:
      # We're at a low point, and we don't have a label
      # yet.
      this.label = string.lowercase[cur_label % 26]
      # logging.info("%d %d %s" % (this.x, this.y, this.label))
      cur_label += 1
      return this.label

  for i in range(height):
    for j in range(width):
      walk(i,j)

  print "Case #%d:" % (case + 1)
  for i in range(height):
    print " ".join(mat[i, j].label for j in range(width))


work()
