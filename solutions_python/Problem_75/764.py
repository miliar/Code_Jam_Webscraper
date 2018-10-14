#!/usr/bin/python

import sys

def combines_with(c1, c2):
   if c1 not in c_h or c2 not in c_h:
      return False
   for p in c_h[c1]:
      if c2 == p[0]:
         return True
   return False

def combines_to(c1, c2):
   for p in c_h[c1]:
      if c2 == p[0]:
         return p[1]
   return None

def any_opposition(s, c1):
   if c1 not in o_h:
      return False
   for c in s:
      if c in o_h[c1]:
         return True
   return False

fp = open(sys.argv[1], 'r')

num_cases = int(fp.readline())

for i in range(0, num_cases):
   c_h = {}
   o_h = {}

   line = fp.readline()
   words = line.split()

   C = int(words.pop(0))
   
   for j in range(0, C):
      s = words.pop(0)
      if s[0] in c_h:
         c_h[s[0]] = c_h[s[0]].append((s[1], s[2]))
      else:
         c_h[s[0]] = [(s[1], s[2])]
      if (s[0] != s[1]):
         if s[1] in c_h:
            c_h[s[1]] = c_h[s[1]].append((s[0], s[2]))
         else:
            c_h[s[1]] = [(s[0], s[2])]

   D = int(words.pop(0))

   for j in range(0, D):
      s = words.pop(0)
      if s[0] in o_h:
         o_h[s[0]] = o_h[s[0]].append(s[1])
      else:
         o_h[s[0]] = [s[1]]
      if s[1] in o_h:
         o_h[s[1]] = o_h[s[1]].append(s[0])
      else:
         o_h[s[1]] = [s[0]]

   length = int(words.pop(0))

   s = words.pop(0)

   curr = ""

   for c in s:
      if len(curr) == 0:
         curr += c
      else:
         c_last = curr[len(curr) - 1]
         if combines_with(c, c_last):
            curr = curr[:len(curr) - 1] + combines_to(c, c_last)
         elif any_opposition(curr, c):
            curr = ""
         else:
            curr += c

   print "Case #" + str(i+1) + ": [" + ", ".join(list(curr)) + "]"
