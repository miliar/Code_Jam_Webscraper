#!/usr/bin/python
import sys, os, numpy as np
def print_usage():
  print "Usage: lawn.py <input file>"

def read_input_file(filename):

  with open(filename) as input_file:
    data = input_file.read()
  data_lines = data.split("\n")
  num_lawns = int(data_lines[0])
  data_lines = data_lines[1:]

  lawns = []
  i = 0
  while i < len(data_lines):
    if len(data_lines[i].replace(" ", "")) == 0:
      i += 1
      continue
    rows_cols = map(int, data_lines[i].split())
    rows = rows_cols[0]
    cols = rows_cols[1]

    lawn = np.empty((rows,cols))
    i += 1
    for j in range(rows):
      lawn[j,:] = map(int, data_lines[i].split())
      i += 1
    lawns.append(lawn)
  return lawns
      


def lawn_is_possible(lawn):
  """
    returns true if the NumPy matrix lawn can be 
    created by moving in consecutive decreasing height (by an entire row or entire column)
  """

  rows, cols = np.shape(lawn)
  # Find unique list of numbers
  nums = {}
  for i in range(rows):
    for j in range(cols):
      if lawn[i,j] not in nums:
        nums[lawn[i,j]] = 1
  sorted_nums = []

  for (key, val) in nums.items():
    sorted_nums.append(key)
  sorted_nums.sort()
  unique_num_count = len(sorted_nums)
  
  # Keep track of which row/col have already been crossed at a particular height
  crossed_rows = [[None]*unique_num_count]*rows
  crossed_cols = [[None]*unique_num_count]*cols

  # Find 
  for i in range(rows):
    for j in range(cols):
      num = lawn[i,j]
      if not crossed_row(lawn, num, i) and not crossed_col(lawn, num, j):
        return "NO"
  return "YES"

def crossed_row(lawn, num, row):
  rows, cols = np.shape(lawn)
  return sum(lawn[row,:]) <= num*cols

def crossed_col(lawn, num, col):
  rows, cols = np.shape(lawn)
  return sum(lawn[:,col]) <= num*rows

def main():
  if len(sys.argv) != 2:
    print_usage()
    sys.exit(1)

  input_filename = sys.argv[1]
  lawns = read_input_file(input_filename)
  for i, lawn in enumerate(lawns):
    print "Case #" + str(i+1) + ": " + lawn_is_possible(lawn)
    

if __name__ == "__main__":
  main()
