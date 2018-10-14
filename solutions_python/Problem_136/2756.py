#! /bin/env python3

import sys

STARTING_RATE = 2.0

def calculate_fastest_win(C, F, X):
  time = 0.0
  current_rate = STARTING_RATE

  if X < C:
    return X / current_rate

  time += C / current_rate

  while X * current_rate < (X - C) * (current_rate + F):
    current_rate += F
    time += C / current_rate

  time += (X - C) / current_rate

  return time

def process_case(infile, outfile, case):
  line = infile.readline()
  C, F, X = map(float, line.split())
  time = calculate_fastest_win(C, F, X)
  outfile.write("Case #{}: {:.7f}\n".format(case, time))

def main():
  input_file_name = sys.argv[1]
  output_file_name = sys.argv[2]

  with open(input_file_name, 'r') as infile:
    with open(output_file_name, 'w') as outfile:
      T = int(infile.readline())
      for case in range(1, T+1):
        process_case(infile, outfile, case)

main()
