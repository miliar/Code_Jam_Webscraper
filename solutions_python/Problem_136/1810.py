#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from collections import namedtuple
Game = namedtuple("Game", ['c', 'f', 'x'])

def parse_input(input_data):
  # parse the input
  lines = input_data.split('\n')
  firstLine = lines[0].split()
  test_cases = int(firstLine[0])
  games = []
  for i in range(1, test_cases+1):
    line = lines[i]
    parts = line.split()
    games.append(Game(float(parts[0]), float(parts[1]), float(parts[2])))
  return games, test_cases

def solve_it(games, test_cases):
  for i in range(1, test_cases+1):
    game=games[i-1]
    rate=2.0
    c=game.c
    f=game.f
    x=game.x
    max_time=x/rate
    time=0.0
    flag=True
    while flag:
      time = time + (c/rate)
      rate = rate + f
      new_time = time + (x/rate)
      if new_time>max_time:
        flag=False
      else:
        max_time=new_time
#      print 'Case #' + str(i) + ': ' + str(max_time) + '\n'
    
    print 'Case #' + str(i) + ': ' + str(max_time) + '\n'
    

import sys
if __name__ == '__main__':
  file_location = sys.argv[1].strip()
  input_data_file = open(file_location, 'r')
  input_data = ''.join(input_data_file.readlines())
  input_data_file.close()
  games, test_cases = parse_input(input_data)
  solve_it(games, test_cases)