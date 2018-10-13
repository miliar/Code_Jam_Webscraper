# -*- coding: utf-8 -*-


t = input()
#print 'ok'
case =1
for i in range(t):
  dic = []
  tot =0
  spc = raw_input()
  spc = spc.split()
  n = int(spc[0])
  m = int(spc[1])
  for j in range(n):
    s = raw_input()
    t = s.split('/')
    q = ''
    for w in t:
      #dic.append(q)
      if w!='':
	q = q+'/'+w
	dic.append(q)
  #print dic
  for j in range(m):
    s = raw_input()
    t = s.split('/')
    
    cnt=0
    q=''
    for w in t:
      if w!='':
	q = q+'/'+w
	if q in dic:
	  cnt=cnt+1
	else: 
	  dic.append(q)
    #print dic
    tot = tot + len(t) - 1 -cnt
  print 'Case #'+str(case)+':',tot
  case = case+1    
    