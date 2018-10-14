#!/usr/bin/env python

input = open('C:\Documents and Settings\Administrator\My Documents\GCJ\Train Times\B-large.in','r')
output = open('C:\Documents and Settings\Administrator\My Documents\GCJ\Train Times\B-large.out','w')

def gettime(str):
  time = map(int,str.split(':'))
  return time[0] * 60 + time[1]

for case in range(int(input.readline())):
  t = int(input.readline())
  na,nb = map(int,input.readline().strip().split(' '))
  
  needed_a = [0 for i in range(na)]
  avail_b = [0 for i in range(na)]
  needed_b = [0 for i in range(nb)]
  avail_a = [0 for i in range(nb)]
  
  for i in range(na):
    needed_a[i],avail_b[i] = map(gettime,input.readline().strip().split(' '))
  
  for i in range(nb):
    needed_b[i],avail_a[i] = map(gettime,input.readline().strip().split(' '))
  
  needed_a.sort()
  needed_b.sort()
  avail_a.sort()
  avail_b.sort()
  
  tot_a,tot_b,pos = 0,0,0
  for i in range(len(needed_a)):
    if pos >= len(avail_a):
      tot_a += 1
    elif needed_a[i] < avail_a[pos] + t:
      tot_a += 1
    else:
      pos += 1
  
  pos = 0
  for i in range(len(needed_b)):
    if pos >= len(avail_b):
      tot_b += 1
    elif needed_b[i] < avail_b[pos] + t:
      tot_b += 1
    else:
      pos += 1
  
  print t
  print needed_a,avail_a,tot_a
  print needed_b,avail_b,tot_b
  
  output.write("Case #%s: %s %s\n" % (case + 1, tot_a, tot_b))

output.close()
input.close()