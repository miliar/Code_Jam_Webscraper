#/bin/python.exe
import sys
""" Did some work on paper. Looks like gorosort(k)
 = number of items in array k not in the right order
"""

def solve_case(line_input):
  array = [int(x) for x in line_input.split(" ")]
  sorted_arr = sorted(array)
  # check number of elements not in place
  return len([x for (x,y) in zip(array, sorted_arr) if x != y])

#main
input_f = open(sys.argv[1])
num_cases = int(input_f.readline())
for c in xrange(1, num_cases+1):
  input_f.readline() #ignore every other line of input
  print "Case #%d: %d.000000" % (c, solve_case(input_f.readline().strip()))

