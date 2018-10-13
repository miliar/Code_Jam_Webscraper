fl = open(r'/home/questworld/Desktop/a.in')
fout = open(r'/home/questworld/Desktop/b.out','w')
numentries = int(fl.readline())
for i in range(1,numentries+1):
  st = fl.readline().replace('\n','') 
  sp = st.split(' ')
  c = float(sp[0])
  f = float(sp[1])
  x = float(sp[2])
  flag = False
  res2 = 0
  res1 = 0
  acquired = 0
  temp = 2
  while flag == False:
    res1 = res1+(x/temp)
    res2 = res2+(c/temp)
    temp = temp +f
    t1 = res2 + (x/temp)
    if res1 <= t1:
      flag = True
      fout.write("Case #"+str(i)+": "+str(res1)+"\n") 
    else:
      res1 = res2
fl.close()
fout.close()
    
          
