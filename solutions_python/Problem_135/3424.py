#!/usr/bin/python

cursor = 1

input = open("input.txt").read().split()

num_cases = int(input[0])

def cur():
   global cursor
   cursor = cursor + 1
   return cursor - 1


for i in range(num_cases):
   ans1 = int(input[cur()])
   board1 = []
   for j in range(4):
      board1.append([])
      for k in range(4):
         board1[j].append(input[cur()])

   ans2 = int(input[cur()])
   board2 = []
   for j in range(4):
      board2.append([])
      for k in range(4):
         board2[j].append(input[cur()])

   result = list(set(board1[ans1-1]) & set(board2[ans2-1]))

   print "Case #%d: %s" % (i+1, result[0] if len(result) == 1 else "Volunteer cheated!" if len(result) < 1 else "Bad magician!")

