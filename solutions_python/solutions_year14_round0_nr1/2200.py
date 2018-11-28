#!/usr/bin/python
with open('A-small-attempt0.in','r') as f:
  data=f.read()
linens = data.splitlines()
linens.reverse()
with open('submit','w') as f:
 for x in range(0,int(linens.pop())):
  row1 = int(linens.pop())
  items1=[]
  for y in range(0,4):
    I = linens.pop();
    if y+1 == row1:
            items1 = [int(i) for i in I.split()]

  row2 = int(linens.pop())
  items2=[]
  for y in range(0,4):
    I = linens.pop();
    if y+1 == row2:
            items2 = [int(i) for i in I.split()]

  matches=[]

  for item1 in items1:
    if item1 in items2:
            matches.append(item1);
  if len(matches) == 1:
          thing = "Case #%d: %d\n" % (x+1,matches[0])
          f.write(thing)
  elif len(matches) == 0:
          thing = "Case #%d: Volunteer cheated!\n" % (x+1)
          f.write(thing)
  else:
          thing = "Case #%d: Bad magician!\n" % (x+1)
          f.write(thing)
