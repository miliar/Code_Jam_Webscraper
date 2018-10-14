import codejam
import numpy
import pdb

class Watershed(codejam.CodeJam):
  def __init__(self):
    NORTH = 1
    WEST = 2
    EAST = 3
    SOUTH = 4
    self.sink = 0
    self.elevation = 0
    self.next_letter = 1

  def solve(self, x, y):
    if self.sink[x,y] != 0:
      return self.sink[x,y]

    min = self.elevation[x,y]
    min_dir = 0
    for i in xrange(1, 5):
      elev_in_dir = self.get_elevation(x, y, i)
      if elev_in_dir == -1:
        continue
      if elev_in_dir < min:
        min = elev_in_dir
        min_dir = i
    if min_dir == 0:
      self.sink[x,y] = self.next_letter
      self.next_letter += 1
    else:
      pos = self.get_position(x, y, min_dir)
      self.sink[x,y] = self.solve(*pos)
    return self.sink[x,y]
  
  def get_elevation(self, x, y, i):
    x, y = self.get_position(x, y, i)
    try:
      elev = self.elevation[x, y]
    except IndexError:
      elev = -1
    if (x == -1) or (y == -1):
      return -1
    return elev

  def get_position(self, x, y, dir):
    if dir is 0:
      return x,y
    if dir is 1:
      return x-1, y
    if dir is 2:
      return x, y-1
    if dir is 3:
      return x, y+1
    if dir is 4:
      return x+1, y
        


  def write_output(self, case):
    self.output.write('Case #%d:\n' % case)
    letters = 'Qabcdefghijklmnopqrstuvwxyz'
    rows, columns = self.sink.shape
    for x in xrange(rows):
      for y in xrange(columns):
        self.output.write('%s ' % letters[int(self.sink[x,y])])
      self.output.write('\n')

  def main(self):
    filename = self.get_filename_arg()
    input = open(filename, 'r')
    self.output = open('output_' + filename, 'w')
    num_cases = int(input.readline())
    for case in xrange(1, num_cases + 1):
      rows, columns = map(int, input.readline().split(' '))
      self.elevation = numpy.empty((rows,columns))
      self.sink = numpy.zeros((rows,columns))
      self.next_letter = 1
      for x in xrange(rows):
        row = input.readline()
        self.elevation[x] = map(int, row.split(' '))
      for x in xrange(rows):
        for y in xrange(columns):
          self.solve(x,y)
      self.write_output(case)
    self.output.close()
    input.close()


if __name__ == "__main__":
  reload(codejam)
  app = Watershed()
  app.main()
