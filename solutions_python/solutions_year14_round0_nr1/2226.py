#!/usr/bin/python

from sys import stdin

def main():
  T = int(stdin.readline())
  for case in range(1, T + 1):
    solve_case(case)

def solve_case(case):
  first_answer = int(stdin.readline())
  first_arrangement = read_arrangement()
  first_candidates = first_arrangement[4 * (first_answer - 1): 4 * first_answer]
  second_answer = int(stdin.readline())
  second_arrangement = read_arrangement()
  second_candidates = second_arrangement[4 * (second_answer - 1): 4 * second_answer]
  candidates = set(first_candidates).intersection(set(second_candidates))
  if len(candidates) == 0:
    answer = "Volunteer cheated!"
  elif len(candidates) == 1:
    answer = str(candidates.pop())
  else:
    answer = "Bad magician!"
  print "Case #%d: %s" % (case, answer)

def read_arrangement():
  cards = []
  for row in range(4):
    cards.extend([int(c) for c in stdin.readline().split()])
  return cards

if __name__ == "__main__":
  main()

