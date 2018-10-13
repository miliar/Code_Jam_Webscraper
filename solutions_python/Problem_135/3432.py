f=open("input")
tries = int(f.readline())
for i in range(tries):
  tab=[]
  linenum=int(f.readline());
  for j in range(4):
    line=f.readline()
    tab.append(line[:-1])
  first = tab[linenum-1].split(" ")
  linenum=int(f.readline());
  tab=[]
  for j in range(4):
    line=f.readline()
    tab.append(line[:-1])
  second=tab[linenum-1].split(" ")
  found=0
  bad=0
  for k in first:
    if k in second:
      if found==0:
        found=1
        result=k
      elif found==1:
        bad=1

  if bad==1:
    print "Case #" + str(i+1) + ": Bad magician!"
  elif found==0:
    print "Case #" + str(i+1) + ": Volunteer cheated!"
  else:
    print "Case #" + str(i+1) + ": " + result
