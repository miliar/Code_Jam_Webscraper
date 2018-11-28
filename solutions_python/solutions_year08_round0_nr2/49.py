#!/usr/bin/python
def sec(s):
  s= s.replace(":", " ")
  l= map(int, s.split())
  return (60*l[0]+l[1], 60*l[2]+l[3])
for c in range(input()):
  turn= input()
  na, nb= map(int, raw_input().split())
  ab=[]
  ba=[]
  for i in range(na):
    ab.append(sec(raw_input()))
  ab.sort()
  for i in range(nb):
    ba.append(sec(raw_input()))
  ba.sort()
  a,b=0,0
  da=[]
  db=[]
  for i in range(len(ab)+len(ba)):
   if len(ba)==0 or (len(ab)!=0 and ab[0][0]<ba[0][0]):
     if len(da)==0 or da[0]>ab[0][0]:
       a=a+1
     else:
       da=da[1:]
     db.append(ab[0][1]+turn)
     db.sort()
     ab= ab[1:]
   else:
     if len(db)==0 or db[0]>ba[0][0]:
       b=b+1
     else:
       db=db[1:]
     da.append(ba[0][1]+turn)
     da.sort()
     ba= ba[1:]
  print "Case #%d: %d %d" % (c+1, a, b)
