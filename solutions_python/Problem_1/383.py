#!/usr/bin/python
for c in range(input()):
  nse= input()
  se= []
  for i in range(nse):
    se.append(raw_input())
  switch= 0
  u= []
  rest= se[:]
  for q in range(input()):
    qu= raw_input()
    if not (qu in u):
      if len(rest)==1:
        switch= switch+1
        to= rest[0]
        u= [to]
        rest= se[:]
        rest.remove(to)
      else:
        u.append(qu)
        rest.remove(qu)
  print "Case #%d: %d" % (c+1, switch)
