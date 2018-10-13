#! /usr/bin/env python
# -*- coding: utf-8 -*-

def beatTheMagic(sample):
   testCases = int(sample[0])
   sample = sample[1:]
   f = open("/opt/gcj/result.txt","w")
   for i in range(testCases):
      firstRow = sample[i * 10 + int(sample[i * 10])].split()
      secondRow = sample[i * 10 + 5 + int(sample[i * 10 + 5])].split()
      hit = list()
      for j in firstRow:
         if j in secondRow:
            hit.append(j)
      if len(hit) == 1:
         f.write("Case #" + str(i + 1) + ":" + hit[0] + "\n")
      elif len(hit) == 0:
         f.write("Case #" + str(i + 1) + " Volunteer cheated!\n")
      elif len(hit) > 1:
         f.write("Case #" + str(i + 1) + " Bad magician!\n")

if __name__ == '__main__':
   f = open("/opt/gcj/testing.txt","r")
   lines = [x.replace('\n','') for x in f.readlines()][:-1]
   f.close()
   beatTheMagic(lines)