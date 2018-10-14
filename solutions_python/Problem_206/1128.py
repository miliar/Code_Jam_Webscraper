#!/usr/bin/python

t = int(raw_input())  # read a line with a single integer

def timeto(i,d,s):
    time=((d-1.0*i)/s)
    return time

def findlong(tab,d):
    max = 0.0
    for i in range(len(tab)):
        (i,s)=tab[i]
        time=timeto(i,d,s)
        if time > max:
            max = time
    return max

def answer(tab,d):
    time = findlong(tab,d)
    spa = (d / time)
    return  '{:.6f}'.format(spa)


for z in xrange(1, t + 1):
  d,k =[int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  tab = []
  for j in range(k):
      i,s = [int(r) for r in raw_input().split(" ")]
      tab.append((i,s))
  print "Case #{}: {}".format(z, answer(tab, d))
