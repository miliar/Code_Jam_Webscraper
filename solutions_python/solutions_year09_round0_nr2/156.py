Location = "B-large.in"

class Cell(object):
  def __init__(self, basinnumber = None):
    self.left = None
    self.right = None
    self.up = None
    self.down = None
    self.number = None
    self.basinletter = None
    self.basinnumber = basinnumber
    self.backtrack = None

  def getLowest(self):
    lowest = self.number
    dir = None
    if self.up != None and self.up.number < lowest:
      lowest = self.up.number
      dir = self.up
    if self.left != None and self.left.number < lowest:
      lowest = self.left.number
      dir = self.left
    if self.right != None and self.right.number < lowest:
      lowest = self.right.number
      dir = self.right
    if self.down != None and self.down.number < lowest:
      lowest = self.down.number
      dir = self.down
    if dir != None:
      basinnumberlowest = min(self.basinnumber, dir.basinnumber)
      dir.basinnumber = basinnumberlowest
      num = dir.getLowest()
      self.basinnumber = num
      return num
    else:
      return self.basinnumber

class Matrix(object):
  def __init__(self, height, width):
    self.height = height
    self.width = width
    basinnumber = 0
    self.first = Cell(basinnumber)
    current = self.first
    current.basinnumber = basinnumber
    for i in range(1, self.width):
      basinnumber = basinnumber + 1
      current.right = Cell(basinnumber)
      current.right.left = current
      current = current.right
    currentfirst = self.first
    for j in range(1, self.height):
      basinnumber = basinnumber + 1
      current = currentfirst
      current.down = Cell(basinnumber)
      current.down.up = current
      current = current.down
      currentfirst = currentfirst.down
      for i in range(1, self.width):
        basinnumber = basinnumber + 1
        current.right = Cell(basinnumber)
        current.right.left = current
        current = current.right
    currentfirst = self.first
    for i in range(1, self.width):
      current = currentfirst
      for j in range(1, self.height):
        current.right.down = current.down.right
        current.down.right.up = current.right
        current = current.down
      currentfirst = currentfirst.right
    self.current = self.first
    lex = "abcdefghijklmnopqrstuvwxyz"
    self.lexlist = []
    lexdict = []
    for l in lex:
      self.lexlist.append(l)
    self.lexdict = {}
    self.lowest = -1

  def addline(self, numbers):
    current = self.current
    current.number = int(numbers[0])
    for i in range(1, len(numbers)):
      current = current.right
      current.number = int(numbers[i])
    self.current = self.current.down

  def printmatrix(self, func):
    currentfirst = self.first
    current = currentfirst
    if func == 0:
      current.getLowest()
    elif func == 1:
      self.convertCurrent(current)
    else:
      printstring = str(current.basinletter)
    for i in range(1, self.width):
      current = current.right
      if func == 0:
        current.getLowest()
      elif func == 1:
        self.convertCurrent(current)
      else:
        printstring = printstring + " " + str(current.basinletter)
    if func == 2:
      output.write(printstring + "\n")
    for j in range(1, self.height):
      currentfirst = currentfirst.down
      current = currentfirst
      if func == 0:
        current.getLowest()
      elif func == 1:
        self.convertCurrent(current)
      else:
        printstring = str(current.basinletter)
      for i in range(1, self.width):
        current = current.right
        if func == 0:
          current.getLowest()
        elif func == 1:
          self.convertCurrent(current)
        else:
          printstring = printstring + " " + str(current.basinletter)
      if func == 2:
        output.write(printstring + "\n")

  def convertCurrent(self, current):
    if current.basinnumber > self.lowest:
      self.lowest = current.basinnumber
      self.lexdict[self.lowest] = self.lexlist.pop(0)
    current.basinletter = self.lexdict[current.basinnumber]

file = open(Location, "r")
output = open("output2", "w")

numberOfTests = file.readline()
for i in range(0, int(numberOfTests)):
  output.write("Case #" + str(i + 1) + ":\n")
  line = file.readline().rstrip()
  hw = line.split(" ")
  height = int(hw[0])
  width = int(hw[1])
  matrix = Matrix(height, width)
  for j in range(0, height):
    numbers = file.readline().rstrip().split(" ")
    matrix.addline(numbers)
  matrix.printmatrix(0)
  matrix.printmatrix(1)
  matrix.printmatrix(2)
file.close()
output.close()
