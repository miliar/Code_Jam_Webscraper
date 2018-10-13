#!/usr/bin/env python
# encoding: utf-8


import sys
import os


def main(argv):
  fp = open(argv[1], "r")
  test_cases = int(fp.readline().strip())
  
  for test in range(test_cases):
    positions = {"O": 1, "B": 1}
    moves_elapsed = 0
    total_moves = 0
    last_action = None
    
    commands = fp.readline().strip()
    for robot, button in zip(list(commands.split(" ")[1::2]), commands.split(" ")[2::2]):
      if not last_action or last_action == robot:
        last_action = robot
        total_moves += abs(int(button) - positions[robot]) + 1
        moves_elapsed += abs(int(button) - positions[robot]) + 1
      else:
        last_action = robot
        if moves_elapsed >= abs(int(button) - positions[robot]):
          moves_elapsed = 1
          total_moves += 1
        else:
          moves_elapsed = abs(int(button) - positions[robot]) + 1 - moves_elapsed 
          total_moves += moves_elapsed
          
      positions[robot] = int(button)
    sys.stdout.write("Case #%d: %d\n" %(test+1, total_moves))
	


if __name__ == '__main__':
	sys.exit(main(sys.argv))

