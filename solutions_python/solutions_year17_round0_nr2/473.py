#! /usr/bin/env python3

import os
import os.path
import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description='tidy')
parser.add_argument("filename", help='Filename')

args = parser.parse_args()

class Number:
  def __init__(self, s):
    self.value = []
    for c in s:
      self.value.append(int(c))

  def __str__(self):
    s = ''
    for v in self.value:
      s += str(v)
    return s

  def decrement(self, index):
    self.value[index] -= 1
    if self.value[index] == -1:
      self.value[index] = 9
      self.decrement(index-1)

  def find(self):
    for i in range(len(self.value))[::-1]:
      #print("i={}:{}".format(i, self.value[i]))
      for j in range(i):
        if self.value[j] > self.value[i]:
          #print("j={}: {}".format(j, self.value[j]))
          for k in range(i, len(self.value)):
            self.value[k] = 9
          self.decrement(i-1)
          #print(str(self))
          break
    while self.value[0] == 0:
      self.value = self.value[1:]


outputfile = os.path.splitext(args.filename)[0] + ".out"

with open(args.filename, 'r') as f:
  with open(outputfile, 'w+') as fout:
    num_tests = int(f.readline().strip())
    for testcase in range(1,num_tests+1):
      number = Number(f.readline().strip())
      print("Case #{} Input: {}".format(testcase, number))
      number.find()
      print("Output: {}".format(str(number)))
      fout.write("Case #{}: {}\n".format(testcase, str(number)))


