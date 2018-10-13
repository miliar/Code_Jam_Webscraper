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


gmap = { "a":"y", "b":"h", "c":"e", "d":"s", "e":"o", "f":"c", "g":"v", "h":"x", "i":"d", "j":"u", "k":"i", "l":"g", "m":"l", "n":"b", "o":"k", "p":"r", "q":"z", "r":"t", "s":"n", "t":"w", "u":"j", "v":"p", "w":"f", "x":"m", "y":"a", "z":"q"} 

# Write your code here
def runtest(numtest):
  string = f_in.readline()
  string.strip()

  newstring = ""

  for ch in string:
    if ch == ' ':
      newstring = newstring + ' '
    elif ch.isalnum():
      newstring = newstring + str(gmap.get(ch))

  output(numtest, newstring)

def main():
  numtests = int(f_in.readline())

  for i in range(1, int(numtests) + 1):
    runtest(i)
    print "Test Case #",i," done"

  f_in.close()
  f_out.close()

main()
