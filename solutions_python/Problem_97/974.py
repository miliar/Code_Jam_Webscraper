import sys

if len(sys.argv) < 2:
  raise RuntimeError("Please give the name of the input file") 

inputfilename = str(sys.argv[1])
outputfilename = inputfilename.replace('in','out')
  
f_in = open(inputfilename, 'r')
f_out = open(outputfilename, 'w')


# A Node in a tree
class Node:
  def __init__ (self, val):
    self.name = val
    self.children = list()
  
  def val_in_children(self, val):
    for child in self.children:
      if child.name.strip() == val.strip():
        return child

    return None

  def print_tree(self):
    for child in self.children:
      print child.name
    
    for child in self.children:
      child.print_tree()


# print the values passed
def output(num_test, value, fileref = f_out):
  fileref.write("Case #"+ str(num_test)+": "+str(value)+"\n")

# Return an n-dimensional array of zeros. Dimensions passed
# as arguments
def zeros(*shape):
  if len(shape) == 0:
    return 0
  car = shape[0]
  cdr = shape[1:]
  return [zeros(*cdr) for i in range(car)]

# Read a line (or multiple lines) from the input.
# If it is a single line then convert into list of ints
# If multiple lines then convert into lists of lists (i.e. 
# two-dimensional array
# If no arguments then reads a single line from f_in
def read_and_convert(linenum = 1, fileref = f_in):

  intlist = list()

  for line in range(0, linenum):  
    strlist = fileref.readline().split()
 
    tmplist = list()  
  
    for string in strlist:
      tmplist.append(int(string))

    if linenum == 1:
      intlist.extend(tmplist)
    else:
      intlist.append(tmplist)
  return intlist


def circular_shift(num):
  
  digits = list()
   
  if num == 0:
    return 0

  while num > 0:
    tmp = num % 10
    num = int((num - tmp)/10)
    digits.append(tmp)

  digits.reverse()
  num = digits.pop(0)
  digits.append(num)

  digits.reverse()

  newnum = 0
  i = 1

  for x in digits:
    newnum = newnum + (x * i)
    i = i * 10

  return newnum

def circular_shift_n(num, n):
  
  for x in range(0,n):
    num = circular_shift(num)

  return num

def num_digits(num):

  count = 0

  if num == 0:
    return 1

  while num > 0:
    tmp = num % 10
    num = int((num - tmp)/10)
    count = count + 1
  
  return count

# Write your code here
def runtest(numtest):

  ranges = read_and_convert()

  A = ranges[0]
  B = ranges[1]
  
  num_dig = num_digits(A)
  count = 0

  mymap = dict()

  for num in range(A, B+1):
    val = num
    for cnt in range(1, num_dig):
      val = circular_shift(val)
      if val >= A and val <= B and val != num and not( (val, num) in mymap or (num, val) in mymap):
        count = count + 1
        mymap[(val,num)] = 1

  output(numtest, count)

def main():
  numtests = int(f_in.readline())

  for i in range(1, int(numtests) + 1):
    runtest(i)
    print "Test Case #",i," done"

  f_in.close()
  f_out.close()

main()
