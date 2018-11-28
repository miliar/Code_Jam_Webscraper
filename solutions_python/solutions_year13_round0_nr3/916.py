__author__ = 'sergeyy'
import time
import math


def isPalin(n):
   s = str(n)
   p = len(s)
   for i in range(int(p/2)):
      if s[i] != s[p-i-1]:
         return False
   return True

def preBuild(b):
   a = 1
   b = math.floor(math.sqrt(b))
   ret = []
   for i in range(a, b+1):
      if isPalin(i) and isPalin(i*i):
         ret.append(i)
   return ret


def solve(a, b):
   cnt = 0
   aa = math.ceil(math.sqrt(a))
   bb = math.floor(math.sqrt(b))
   for i in m:
      if i >= aa and i<=bb:
         cnt = cnt+1
      if i > bb:
         break
   return str(cnt)

time.clock()

m = preBuild(100000000000000)
with open('input.txt', 'r') as fin:
   with open('output.txt', 'w') as fout:
      cnt = int(fin.readline())
      for case in range(1, cnt+1):
         a, b = [int(x) for x in fin.readline().split()]
         oline = ''
         oline = 'Case #' + str(case) +': ' + solve(a,b) +'\n'
         fout.write(oline)
print (time.clock())




