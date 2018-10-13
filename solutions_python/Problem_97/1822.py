#!/usr/bin/env python

loop=int(raw_input())
result=''
for i in range(loop):
  result+="Case #%d: " % (i+1)
  s=raw_input().split(' ')
  r = list( [ str(i) for i in range(int(s[0]), (int(s[1])+1))  ] )
  r1 = r
  num = 0
  isto=[]
  for p in range(len(r)):
    po = r1.pop()
    length = len(po)
    for xi in range(length-1):
      x = xi+1
      stri = po[x:]+po[:x]
      v = (stri,po) if int(stri) < int(po) else (po,stri)
      if v[0] in r1:
        if v in isto:
          # print 'check ' + str(v)
          pass
        else:
          num = num + 1
          isto.append(v)

  result+="%d\n" % (num)

print result







