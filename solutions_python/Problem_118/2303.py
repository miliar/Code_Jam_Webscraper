#!/usr/bin/python -tt
import math

def pal(num):
 s = str(num)
 b = -1
 for a in range(len(s)):
  if s[a] != s[b]:return False
  b -=1
 return True

def check(tpl):
 s = tpl[0]
 e = tpl[1]
 result = 0
 palin = int(math.sqrt(s))
 for i in range (s,e+1):
  if i % 10 == 0 : continue
  sqr = palin*palin
  if palin > 10:
   if sqr > e: return result
   sqr = palin*palin
   if ((sqr >= s) & (sqr <= e)):
    if ((pal(sqr)) & (pal(palin))) :
     result+=1
  else:
   if ((i == 1) or (i == 4) or (i == 9)):
    result+=1
  palin+=1
 return result

lines = input()
count = 0
for i in range(lines):
 count+=1
 ls = raw_input()
 ls = ls.split()
 tpl = int(ls[0]),int(ls[1])
 print 'Case #'+str(count)+': '+str(check(tpl))