file = open("B-large.in")
write = open("result", 'w')
i = 0
c = 0
f = 0
x = 0
t1 = 0
t = 0
for line in file:
  line = line.replace('\n', '')
  if i == 0:
    pass
  else:
    c = float(line.split(' ')[0])
    f = float(line.split(' ')[1])
    x = float(line.split(' ')[2])
    for n in range(0,1000000):
      if n == 0:
        t = x/(2+f*n)
      else:
        t1 += c/(2+(n-1)*f)
        t = min(x/(2+f*n) + t1, t)
    write.write("Case #" + str(i) + ": " + "{0:.7f}".format(t) + '\n')
    write.flush()
  t1 = 0
  i +=1


    
