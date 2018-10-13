f = open(r'/home/questworld/Desktop/a.in')
fout = open(r'/home/questworld/Desktop/b.out','w')
numentries = int(f.readline())
for i in range(1,numentries+1):
  readrow = int(f.readline())
  k1 = ''
  for j in range(0,4):
    if j+1==readrow:
      k1 = f.readline().replace('\n','')
    else:
      f.readline()
  k2 = ''
  readrow1 = int(f.readline())
  for j in range(0,4):
    if j+1 == readrow1:
      k2 = f.readline().replace('\n','')
    else:
      f.readline()
  s1 = k1.split(' ')
  s2 = k2.split(' ')
  s3 = set(s1)
  s4 = set(s2)
  res = s3&s4
  p = len(res)
  if p==1:
    fout.write('Case #'+str(i)+': '+res.pop()+'\n')
  elif p>1:
    fout.write('Case #'+str(i)+': Bad magician!\n')
  else:
    fout.write('Case #'+str(i)+': Volunteer cheated!\n')
f.close()
fout.close()
  
      

         
