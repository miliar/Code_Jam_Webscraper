#! /bin/env python3

import sys

def find_largest_fitting(sizes, space):
  for i, size in enumerate(sizes):
    if size <= space:
      return (i, size)
  return (None, None)

def count_discs(N, X, sizes):
  print("N: {}, X: {}, sizes: {}".format(N, X, sizes))
  sizes = sorted(sizes, reverse=True)
  discs = 0
  while len(sizes) > 0:
    first = sizes[0]
    (idx, second) = find_largest_fitting(sizes[1:], X - first)
    if idx is not None:
      del sizes[idx + 1]
    del sizes[0]
    discs += 1
    print("disc {}: {} + {}".format(discs, first, second))
  return discs

def process_case(infile, outfile, case):
  N, X = map(int, infile.readline().split())
  sizes = list(map(int, infile.readline().split()))
  answer = count_discs(N, X, sizes)
  outfile.write("Case #{}: {}\n".format(case, answer))

def main():
  input_file_name = sys.argv[1]
  output_file_name = sys.argv[2]

  with open(input_file_name, 'r') as infile:
    with open(output_file_name, 'w') as outfile:
      T = int(infile.readline())
      for case in range(1, T+1):
        process_case(infile, outfile, case)

main()
