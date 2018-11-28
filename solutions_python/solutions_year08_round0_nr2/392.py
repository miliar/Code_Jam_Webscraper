def tomin(s):
  s= s.replace(":", " ")
  h= map(int, s.split())
  return (60*h[0]+h[1], 60*h[2]+h[3])
for c in range(input()):
  turn= input()
  na, nb= map(int, raw_input().split())
  tob=[]
  toa=[]
  for i in range(na):
    tob.append(tomin(raw_input()))
  for i in range(nb):
    toa.append(tomin(raw_input()))
  tob.sort()
  toa.sort()
  a=0
  b=0
  da=[]
  db=[]
  for i in range(len(tob)+len(toa)):
   if len(toa)==0 or (len(tob)!=0 and tob[0][0]<toa[0][0]):
     if len(da)==0 or da[0]>tob[0][0]:
       a=a+1
     else:
       da=da[1:]
     db.append(tob[0][1]+turn)
     db.sort()
     tob= tob[1:]
   else:
     if len(db)==0 or db[0]>toa[0][0]:
       b=b+1
     else:
       db=db[1:]
     da.append(toa[0][1]+turn)
     da.sort()
     toa= toa[1:]
  print "Case #%d: %d %d" % (c+1, a, b)
