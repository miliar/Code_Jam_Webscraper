
__author__ = 'sergeyy'
import time
import numpy as np

def getUsedH(a):
   res = set()
   for l in a:
      res = res | set(l)

   return res

def delLine(a, l):
   del a[l]
   return a

def delColl(a, c):
   for l in a:
      del l[c]
   return a

def isCuutbl(line):
   if line[0] >= max(line):
      return True
   return False

def removeH(a,h):
   if min([min(x) for x in a]) < h:
      return False
   while True:
      lToRem = []
      cToRem = []

      for i in range(len(a)):
         if (a[i][0] == h):
            if isCuutbl(a[i]):
               lToRem.append(i);

      for i in range(len(a[0])):
         if (a[0][i] == h):
            if isCuutbl([x[i] for x in a]):
               cToRem.append(i);

      if not lToRem and not cToRem:
         return a

      for i in sorted(lToRem, reverse=True):
         delLine(a, i)

      for i in sorted(cToRem, reverse=True):
         delColl(a, i)
      if not a:
         return a


def solve(a):

   for h in getUsedH(a):
      a = removeH(a,h)
      if a == False:
         return 'NO'

   if a:
      return 'NO'
   return 'YES'


with open('input.txt', 'r') as fin:
   with open('output.txt', 'w') as fout:
      cnt = int(fin.readline())
      for case in range(1, cnt+1):
         n, m = [int(x) for x in fin.readline().split()]
         a = [[]*m]*n
         for i in range(n):
            a[i] = [int(x) for x in fin.readline().split()]
         oline = ''
         oline = 'Case #' + str(case) +': ' + solve(a) +'\n'
         fout.write(oline)
print (time.clock())



