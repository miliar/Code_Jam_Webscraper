#!/opt/local/bin/python

import sys, string
import psyco
psyco.full()

def find_max(v):
  max = -9000000
  ind = -1
  for j in range(0, len(v.list)):
    if int(v.list[j]) > max:
      max = int(v.list[j])
      ind = j
  return (max, ind)
def find_min(v):
  min = 9000000
  ind = -1
  for j in range(0, len(v.list)):
    if int(v.list[j]) < min:
      min = int(v.list[j])
      ind = j
  return (min, ind)

input_f = open(sys.argv[1],'r')
count = 1

first_line = input_f.readline()
n_pb = string.atoi(first_line)

for z in range(0, n_pb):
  print "Case #" + str(count) + ":",  ##########
  count = count + 1
  l = string.split(input_f.readline())
  p = int(l[0])
  nk = int(l[1])
  nl = int(l[2])
  l = string.split(input_f.readline())
  freq = []
  for i in range(0, len(l)):
    freq.append(int(l[i]))
  freq.sort()
  #print p
  #print nk
  #print nl
  #print freq
  ret = 0
  for i in range(1, p + 1):
    #print " IIIII : " + str(i)
    for j in range(1, nk + 1):
      #print " JJJJJJ : " + str(j)
      if len(freq) > 0:
        ret = ret + i * freq.pop()
        #print ret

  if len(freq) > 0:
    print "Impossible"
  else:
    print str(ret)

    

