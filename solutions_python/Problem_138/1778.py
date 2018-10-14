#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from collections import namedtuple
Block = namedtuple("Block", ['index', 'value'])

def parse_input(input_data):
  # parse the input
  lines = input_data.split('\n')
  firstLine = lines[0].split()
  test_cases = int(firstLine[0])
  for i in range(1, test_cases+1):
    n = int(lines[3*i-2])
    blocks_naomi = []
    blocks_ken = []
    line_naomi = lines[3*i-1]
    line_ken = lines[3*i]
    parts_naomi = line_naomi.split()
    parts_ken = line_ken.split()
    for j in range(1, n+1):
      blocks_naomi.append(Block(int(j-1), float(parts_naomi[j-1])))
      blocks_ken.append(Block(int(j-1), float(parts_ken[j-1])))
    
    play_ken, score_war = solve_war(blocks_naomi, blocks_ken, n)
    score_deceit_war = solve_deceit_war(blocks_naomi, play_ken, n)
    
    print 'Case #'+str(i)+': '+str(score_deceit_war)+' '+str(score_war)+'\n'

def solve_war(naomi, ken ,n):
  naomi = sorted(naomi, key=lambda k:k.value, reverse=True)
  ken = sorted(ken, key=lambda k:k.value, reverse=True)
  count = 0
  j = 0
  play_ken = []
#  output_data = '\n'.join(map(str, naomi))+'\n\n'
#  output_data += '\n'.join(map(str, ken))+'\n\n'
  for i in range(len(naomi)):
    if(naomi[i].value>ken[j].value):
      count += 1
      play_ken.append(ken.pop())
    else:
      j += 1
      play_ken.append(ken[j-1])
#  print str(count)
#  output_data = '\n'.join(map(str, play_ken))+'\n\n'
#  print output_data
  return play_ken, count

def solve_deceit_war(naomi, ken ,n):
  naomi = sorted(naomi, key=lambda k:k.value, reverse=True)
  count = 0
  j = 0
  output_data = '\n'.join(map(str, naomi))+'\n\n'
  output_data += '\n'.join(map(str, ken))
  for i in range(n):
    if(naomi[j].value>ken[i].value):
      for k in range(1, len(naomi)+1):
        if(naomi[len(naomi)-k].value>ken[i].value):
          count += 1
          naomi.pop(len(naomi)-k)
          break
#  print str(count)
#  print output_data
  return count
  
import sys
if __name__ == '__main__':
  file_location = sys.argv[1].strip()
  input_data_file = open(file_location, 'r')
  input_data = ''.join(input_data_file.readlines())
  input_data_file.close()
  parse_input(input_data)