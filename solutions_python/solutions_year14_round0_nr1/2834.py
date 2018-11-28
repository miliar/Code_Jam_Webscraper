#! /bin/env python3

import sys

ROWS = 4

def read_rows(infile):
  rows = []
  for i in range(ROWS):
    values = map(int, infile.readline().split())
    rows.append(values)
  return rows

def process_case(infile, outfile, case):
  answer1 = int(infile.readline())
  row1 = set(read_rows(infile)[answer1 - 1])
  print(answer1, row1)
  answer2 = int(infile.readline())
  row2 = set(read_rows(infile)[answer2 - 1])
  print(answer2, row2)
  inters = row1 & row2
  outfile.write("Case #{}: ".format(case))
  if len(inters) == 0:
    outfile.write("Volunteer cheated!")
  elif len(inters) == 1:
    guessed_element = list(inters)[0]
    outfile.write("{}".format(guessed_element))
  else:
    outfile.write("Bad magician!")
  outfile.write("\n")

def main():
  input_file_name = sys.argv[1]
  output_file_name = sys.argv[2]

  with open(input_file_name, 'r') as infile:
    with open(output_file_name, 'w') as outfile:
      T = int(infile.readline())
      for case in range(1, T+1):
        process_case(infile, outfile, case)

main()
