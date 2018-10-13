from time import time
import math

inp = open('b.in', 'r+')
out = open('b.out', 'w')

T = int(inp.readline())

for t in range(T):
  s = inp.readline().strip().split(' ')
  N, P = int(s[0]), int(s[1])
  required = [int(i) for i in inp.readline().strip().split(' ')]
  packages = []
  for n in range(N):
    packages.append(sorted([int(i) for i in inp.readline().strip().split(' ')]))

  o = 0
  giveUp = False
  while not giveUp:
    rmi = None
    rma = None
    guilting = None
    guiltyn = None
    guiltylen = None
    restart = False
    goods = 0
    #print "Start", packages
    for ing in range(N):
      #print "Ing", ing
      while True:
        #print ing, packages
        if len(packages[ing]) == 0:
          giveUp=True
          break # give up

        mi = int(math.ceil((packages[ing][0])/(required[ing]*1.1)))
        ma = int((packages[ing][0])/(required[ing]*.9))
        le = ma - mi
        #print mi, ma, packages[ing][0]
        if mi > ma:
          #print "Unusable"
          del packages[ing][0]
          continue
        else:
          if ing == 0:
            # First item
            rmi = mi
            rma = ma
            guilting = ing
            guiltylen = le
            goods += 1
            break
          else:
            if ma < rmi:
              # this item is bad, we can never use it
              #print "Low"
              del packages[ing][0]
              continue
            else:
              if mi > rma:
                # guilty item is bad, delete
                #print "High", guilting, packages
                del packages[guilting][0]
                restart = True
                break
              else:
                # good item, we can continue
                #print "Good"
                if mi > rmi:
                  rmi = mi
                if ma < rma or (ma == rma and le < guiltylen):
                  rma = ma
                  guilting = ing
                  guiltylen = le
                goods += 1
                break
      if restart:
        #print "Re"
        break
      if giveUp:
        #print "GU"
        break
    ##print packages
    if goods == N:
      # got through
      for ing in range(N):
        del packages[ing][0]
      o += 1
      #print "SUCCESS", o
    #print "EE", ing, N, "\n\n"


  out.write("Case #"+str(t+1)+": "+str(o)+"\n")

out.close()