with open("A-small-attempt1.in", 'r') as file:
    data = file.read()

lines = data.splitlines()
Ntests = int(lines[0])

for i in range(Ntests):
  ans1 = int(lines[1 + i*10])
  ans2 = int(lines[6 + i*10])
  
  set1 = set([int(j) for j in lines[1 + ans1 + i*10].split()])
  set2 = set([int(j) for j in lines[6 + ans2 + i*10].split()])
  
  #import ipdb; ipdb.set_traxce()
  
  inter = set1.intersection(set2)
  
  if len(inter) == 1:
    print ''.join(['Case #',str(i+1),':']), inter.pop()
  elif len(inter) > 1:
    print ''.join(['Case #',str(i+1),':']), 'Bad magician!'
  elif len(inter) == 0:
    print ''.join(['Case #',str(i+1),':']), 'Volunteer cheated!'
  
  
