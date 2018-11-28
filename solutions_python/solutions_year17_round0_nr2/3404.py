#!/usr/bin/env python3

import sys

def main():
  fi = sys.stdin
  fo = sys.stdout
  case_count = int(fi.readline().strip())
  for i in range(1, case_count+1):
    n = read_input(fi)
    solution = solve(n)
    display_and_clear(fo, i, solution)

def read_input(f):
  n = f.readline().strip()
  return n

def display_and_clear(f, i, digits):
  s = ''.join([str(d) for d in digits])
  f.write('Case #%d: %s\n' % (i, s))
  f.flush()

def solve(n):
  n = [int(ch) for ch in n]
  length = len(n)

  last_valid_index = 0
  for i in range(1, length):
    if n[i] >= n[last_valid_index]:
      last_valid_index += 1
    else: break

  if last_valid_index == length - 1:
    return n

  # backtrack
  max_valid_digit = n[last_valid_index] - 1
  split_index = 0
  for i in range(0, last_valid_index + 1):
    if n[i] <= max_valid_digit:
      split_index += 1
    else: break


  if split_index == 0 and n[0] == 1:
    # digit count decreases
    return [9 for i in range(length - 1)]
  else:
    n[split_index] -= 1
    return n[:split_index+1] + [9 for i in range(length - split_index - 1)]

if __name__ == '__main__':
  main()


