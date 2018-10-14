#!/usr/bin/env python

import sys

def main():
  filename = "B-small.in"
  f = open(filename, 'r')
  T = int(f.readline().replace('\n',''))
  for i in range(T):
    H, W = map(int, f.readline().replace('\n', '').split(' '))
    b = Basin(H, W)
    for j in range(H):
      heights = f.readline().replace('\n', '').split(' ')
      for k in range(W):
        b.grid[j][k] = heights[k]
    # Grid is now complete
    b.labels[0][0] = 'a'
    # Label north-west position 'a'
    for j in range(H):
      for k in range(W):
        coordinates = [] # Coordinates
        coord = Coordinate(j, k)
        """
        Continue until
        1. Encounter a letter
          Label all letters along the path with this letter
        2. Encounter a sink
          a. Get first letter not used, label all letters
        """
        while coord is not None:
          coordinates.append(coord)
          coord = b.get_next_coordinate(coord)

        b.make_or_expand_path(coordinates)
    print "Case #%d:" % (i+1)
    print b

class Coordinate:
  def __init__(self, y, x):
    self.y = y
    self.x = x

class Basin:
  def get_next_coordinate(self, coordinate):
    x = coordinate.x
    y = coordinate.y
    """Check for border cases
    Check for lower altitude at each one"""
    min = self.grid[y][x]
    has_another = False
    """ [ [a,a,a], [a,a,a], [a,a,a], ]
        y xxx     xxx
    """
    # North
    if y > 0:
      if self.grid[y-1][x] < min:
        min = self.grid[y-1][x]
        coord = Coordinate(y-1, x)
        has_another = True

    # West
    if x > 0:
      if self.grid[y][x-1] < min:
        min = self.grid[y][x-1]
        coord = Coordinate(y, x-1)
        has_another = True

    # East
    if x < self.W - 1:
      if self.grid[y][x+1] < min:
        min = self.grid[y][x+1]
        coord = Coordinate(y, x+1)
        has_another = True

    # South
    if y < self.H - 1:
      if self.grid[y+1][x] < min:
        min = self.grid[y+1][x]
        coord = Coordinate(y+1, x)
        has_another = True

    if has_another:
      return coord
    else:
      return None

  def make_or_expand_path(self, coordinates):
    """Use cur_letter
    Then incr cur_letter"""
    last_coordinate = coordinates[len(coordinates) - 1]
    letter = self.get_label(coordinates)
    if letter is None:
      self.set_path_to_letter(coordinates, self.letters[self.cur_letter])
      self.cur_letter += 1
    else:
      self.set_path_to_letter(coordinates, letter)

  def get_label(self, coordinates):
    for coordinate in coordinates:
      if self.labels[coordinate.y][coordinate.x] is not None:
        return self.labels[coordinate.y][coordinate.x]
    return None

  def set_label(self, coordinate, letter):
    self.labels[coordinate.y][coordinate.x] = letter

  def set_path_to_letter(self, coordinates, letter):
    for coordinate in coordinates:
      self.set_label(coordinate, letter)

  def __init__(self, H, W):
    self.grid = []
    for i in range(H):
      self.grid.append([])
      for j in range(W):
        self.grid[i].append(None)

    self.labels = []
    for i in range(H):
      self.labels.append([])
      for j in range(W):
        self.labels[i].append(None)

    self.H = H
    self.W = W
    self.letters = "abcdefghijklmnopqrstuvwxyz"
    self.cur_letter = 1

  def __str__(self):
    s = ""
    lines = []
    for i in range(self.H):
      for j in range(self.W):
        s += "%s " % self.labels[i][j]
      lines.append(s)
      s = ""
    return "\n".join(lines)

if __name__ == "__main__": main()
