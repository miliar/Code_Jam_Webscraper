"""
  This code includes the cycleSort function
  available from http://en.wikipedia.org/w/index.php?title=Cycle_sort&oldid=423919983
  It is under the Creative Commons Attribution-ShareAlike License
  
  This code is under Creative Commons Attribution Share-Alike License 3.0
  For more information, see: http://creativecommons.org/licenses/by-sa/3.0/legalcode
"""

import sys
filename = 'input.txt'
if len(sys.argv) > 1:
  filename = sys.argv[1]
  
def num_test_cases():
  return int(open(filename).readline())
  
def get_lines():
  f_in = open(filename)
  lines = f_in.readlines()
  lines = [line.strip() for line in lines]
  return lines[1:]

# Sort an array in place and return the number of writes.
def cycleSort(array):
  writes = 0
 
  # Loop through the array to find cycles to rotate.
  for cycleStart in range(0, len(array) - 1):
    item = array[cycleStart]
 
    # Find where to put the item.
    pos = cycleStart
    for i in range(cycleStart + 1, len(array)):
      if array[i] < item:
        pos += 1
 
    # If the item is already there, this is not a cycle.
    if pos == cycleStart:
      continue
 
    # Otherwise, put the item there or right after any duplicates.
    while item == array[pos]:
      pos += 1
    array[pos], item = item, array[pos]
    writes += 1
 
    # Rotate the rest of the cycle.
    while pos != cycleStart:
 
      # Find where to put the item.
      pos = cycleStart
      for i in range(cycleStart + 1, len(array)):
        if array[i] < item:
          pos += 1
 
      # Put the item there or right after any duplicates.
      while item == array[pos]:
        pos += 1
      array[pos], item = item, array[pos]
      writes += 1
 
  return writes

def solve(line):
  return cycleSort([int(x) for x in line.split(' ')])

def main():
  lines = get_lines()
  new_lines = []
  for i, line in enumerate(lines):
    if i%2 == 1:
      new_lines.append(line)
  for (i, line) in enumerate(new_lines):
    expected = solve(line)
    print "Case #%s: %s.000000" % (i+1, expected)

if __name__ == '__main__': main()
