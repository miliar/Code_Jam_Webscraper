#!/usr/bin/python

def isrecycled(n,m):
  sa=str(n)
  sb=str(m)
  i=1
  while i < len(sb):
    #print sa[i:len(sa)],sa[0:i]
    x="".join([sa[i:len(sa)],sa[0:i]])
    #print x
    if int(x)==m:
      return 1
    i+=1

  return 0

def count(A,B):
  count=0

  for i in range(A,B+1):
    for j in range(i+1,B+1):
      if isrecycled (i,j):
        count+=1
  return count

f=open("C-small-attempt2.in", "r")
#f=open("input2.txt")
text=f.read()

lines=text.split("\n")
#print lines[0]
i=1
for line in lines[1:len(lines)-1]:
  
  Numbers = line.split(" ")
  A=int(Numbers[0])
  B=int(Numbers[1])
  print 'Case #{0}: {1}'.format(i, count(A,B))
  i+=1


