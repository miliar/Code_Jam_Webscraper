#!/usr/bin/python

t=input()
for i in xrange(t):
  r,c=map(int,raw_input().strip().split())
  cake=[]
  for j in xrange(r):
    cake.append(list(raw_input().strip()))
    if len(cake[-1])!=c:
      raise "incorrect cake line length "+str(len(cake[-1]))+" s.b. "+str(c)+" row "+str(j)+" case "+str(i)
  #First pass - solve all rows with letters
  for j in xrange(r):
    if cake[j].count("?")<c:
      for ltr in cake[j]:
        if ltr!="?":
          kid=ltr
          break
      for k in xrange(c):
        if cake[j][k]=="?":
          cake[j][k]=kid
        else:
          kid=cake[j][k]
  #Second pass - solve rows with no letters
  for j in xrange(r):
    if cake[j][0]!="?":
      copyrow=j
      break
  for j in xrange(r):
    if cake[j][0]=="?":
      cake[j]=cake[copyrow]
    else:
      copyrow=j
  print "Case #"+str(i+1)+":"
  for j in xrange(r):
    print "".join(cake[j])

