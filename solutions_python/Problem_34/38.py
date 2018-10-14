
import sys
import re

L,D,N = map(int,raw_input().split())
w=[]
for i in range(D):
  w.append(raw_input())
t = []
for case_index in range(1, 1+N):
  sys.stderr.write(str(case_index)+' ')  
  p=raw_input()
  p=p.replace('(','[')
  p=p.replace(')',']')
  prog = re.compile(p)
  res =0
  for x in w:
    if prog.match(x):
      res+=1
  print 'Case #%s: %s'%(case_index,res)

sys.stderr.write('\n')
