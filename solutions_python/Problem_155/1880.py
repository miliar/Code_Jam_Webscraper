#!/usr/bin/python3
import sys
from collections import namedtuple 

def case(line):
  max_shyness,syness_str = line.split(' ')
  shyness = dict(zip(range(int(max_shyness) + 1), (int(c) for c in syness_str)))
  return shyness

def cases(lines):
  return (case(line) for line in lines if line)

def main(filename):
  with open(filename, 'r') as input_file:
    lines = input_file.read().split('\n')
    number_of_cases = int(lines[0])
    for i,case in zip(range(1,number_of_cases+1), cases(lines[1:])):
      #print("Case #{}: {}".format(i, case))
      print("Case #{}: {}".format(i, solve(case)))

def solve(case):
  """A simple greedy algorithm that determines the amount it takes to get to the next level"""
  number_of_people_applauding = case[0]
  number_of_extra_people_required = 0
  for shyness_level in list(case.keys())[1:]:
    extra_friends = 1 if number_of_people_applauding < shyness_level else 0
    number_of_extra_people_required += extra_friends
    number_of_people_applauding += extra_friends + case[shyness_level]
  return number_of_extra_people_required

main("in.dat")
